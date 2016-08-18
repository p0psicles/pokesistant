#!/usr/bin/env python

from __future__ import unicode_literals

import os
import time
from urlparse import urljoin
time.sleep(3)
import sys
import sqlite3, os
from requests.exceptions import (ConnectionError, HTTPError)

sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), 'lib')))
sys.path.append('libs')


from lib.pokemongo.api import PokeAuthSession
from lib.pokemongo.location import Location
from lib.pokemongo.pokedex import pokedex, move_list
from lib.pokemongo.custom_exceptions import GeneralPogoException

from flask import Flask, session, redirect, url_for, \
     abort, render_template, flash, jsonify, request

from contextlib import closing
from passlib.hash import md5_crypt
from operator import itemgetter
import logging

# create our little application :)
app = Flask(__name__,
            template_folder='public',
            static_folder='public',
            static_url_path='')

# Load default config and override config from an environment variable
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='pikapika',
    STORE={},
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

DEBUG = True
STARTED = ""
STARTEDTHREAD = ""
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

def setupLogger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('Line %(lineno)d,%(filename)s - %(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)


def get_pogo_auth(username=None, password=None, auth='google'):
    # Create PokoAuthObject

    if (not username or not password) and not app.config['STORE'].get(session.get('username')):
        abort(401)

    if username and password:
        # Create a new session
        auth = PokeAuthSession(
            username,
            password,
            auth,
        )
        pogo_session = auth.authenticate()
        app.config['STORE'][username] = {'session': pogo_session, 'last_update': time.time()}
    else:
        # reuse old
        pogo_session = app.config['STORE'][session.get('username')].get('session')

    return pogo_session


def check_refresh_session(timeout=1800):
    username = session.get('username')
    password = session.get('password')
    auth = session.get('auth')

    if (username and
        app.config['STORE'].get(username) and
            app.config['STORE'][username].get('last_update') + timeout < time.time()):
        return get_pogo_auth(username, password, auth)
    else:
        return get_pogo_auth()


@app.route('/getPokemon', methods=['GET'])
def getpokemon():

    pogo_session = check_refresh_session()

    if not pogo_session:
        return redirect(url_for('openApp'))

    party = pogo_session.getInventory().party
    pokemons = []
    attributes = ['id', 'cp', 'stamina', 'stamina_max', 'move_1', 'move_2', 'individual_attack',
                  'individual_defense', 'individual_stamina', 'nickname', 'pokemon_id', 'num_upgrades',
                  'is_egg', 'battles_attacked', 'battles_defended', 'additional_cp_multiplier',
                  'creation_time_ms', 'cp_multiplier', 'weight_kg']
    for pokemon in party:
        pokemon_attributes = {}
        for attr in attributes:
            pokemon_attributes[attr] = getattr(pokemon, attr)
        pokemon_attributes['pokemon_name'] = pokedex[pokemon_attributes['pokemon_id']]
        pokemon_attributes['IV'] = round((getattr(pokemon, 'individual_attack') +
                                         getattr(pokemon, 'individual_defense') +
                                         getattr(pokemon, 'individual_stamina')) * (100/45.0), 0)
        pokemon_attributes['image_nr'] = str(pokemon_attributes['pokemon_id']).zfill(3)
        pokemon_attributes['move_1_desc'] = move_list[pokemon_attributes['move_1']]
        pokemon_attributes['move_2_desc'] = move_list[pokemon_attributes['move_2']]

        pokemons.append(pokemon_attributes)

    if pokemons:
        #logging.info(str(pokemons))
        return jsonify(pokemons=sorted(pokemons, key=lambda k: k['IV'], reverse=True))
    return []


@app.route('/getPogoSession', methods=['POST'])
def get_pogo_session():
    """This route was intended for doing the login, and then store the pogo_session object
    in a session. But unfortunatly because the object is not serializable this is not possible."""

    error = False
    error_msg = ''

    auth = request.json.get('auth', 'google').encode('utf-8')
    username = request.json.get('username').encode('utf-8')
    password = request.json.get('password').encode('utf-8')

    if not username or not password:
        return jsonify({'error': 'need username and password'})

    # Check service
    if auth not in ['ptc', 'google']:
        logging.error('Invalid auth service {0}'.format(auth))
        sys.exit(-1)

    session['username'] = username
    session['password'] = password
    session['auth'] = auth

    try:
        pogo_session = get_pogo_auth(username, password, auth)
        access_token = pogo_session.accessToken
    except (ConnectionError, HTTPError, GeneralPogoException) as e:
        error = True
        error_msg = e
        pogo_session = None
        access_token = ''

    if pogo_session:
        session['access_token'] = {'last_update': time.time(), 'token': pogo_session.accessToken}

    return jsonify({'authenticated': bool(pogo_session), 'accessToken': access_token,
                    'error': error, 'error_msg': str(getattr(error_msg, 'message', ''))})


@app.route('/getSession', methods=['GET'])
def get_session():
    return jsonify({'username': session.get('username', ''),
                    'password': session.get('password', ''),
                    'auth': session.get('auth', '')})

'''
Basic Web functions Login/Logoff
'''


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            if username == 'admin' and password == app.config['PASSWORD']:
                session['logged_in'] = True
                return redirect(url_for('index'))
            else:
                error = 'Invalid password'
                session['logged_in'] = False
        else:
            error = 'Wrong credentials provided'
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')


@app.route('/', methods=['GET', 'POST'])
def openApp():
    return render_template('templates/index.html')

if __name__ == '__main__':
    # Process arguments
    app.debug = True
    setupLogger()

    arguments = sys.argv
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        print("Starting on port: [%s]" % (int(sys.argv[1])))
        port = 8080
    else:
        pass

    if len(sys.argv) > 2:
        port = int(sys.argv[1])
        print("Starting on port: [%s]" % (int(sys.argv[1])))
        if sys.argv[2].split("=")[0] == "debug":
            app.debug = str2bool(sys.argv[2].split("=")[1])
            print("Starting with Debug: [%s]" % (bool(sys.argv[2].split("=")[1])))
    else:
        port = 8080

    app.run(port=port, host='0.0.0.0', use_reloader=False)
