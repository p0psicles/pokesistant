import os
import time
from urlparse import urljoin
time.sleep(3)
if os.name in ('posix',):
    import sys
    sys.setdefaultencoding("utf-8")
    import site
else:
    import sys
import sqlite3, os

sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), 'lib')))
sys.path.append('libs')

from lib.pokemongo.api import PokeAuthSession
from lib.pokemongo.location import Location
from lib.pokemongo.pokedex import pokedex

from flask import Flask, session, redirect, url_for, \
     abort, render_template, flash, jsonify, request
from contextlib import closing

#from main import *
from passlib.hash import md5_crypt
from operator import itemgetter
import logging

# Testing UTF-8
print sys.getdefaultencoding()

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
    slots={},
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


def get_pokemon(username, password, auth='google'):

    # Create PokoAuthObject
    poko_session = PokeAuthSession(
        username,
        password,
        auth,
    )

    pogo_session = poko_session.authenticate()

    party = pogo_session.checkInventory().party
    pokemons = []
    attributes = ['id', 'cp', 'stamina', 'stamina_max', 'move_1', 'move_2', 'individual_attack',
                  'individual_defense', 'individual_stamina', 'nickname', 'pokemon_id', 'num_upgrades',
                  'is_egg', 'battles_attacked', 'battles_defended', 'additional_cp_multiplier']
    for pokemon in party:
        pokemon_attributes = {}
        for attr in attributes:
            pokemon_attributes[attr] = getattr(pokemon, attr)
        pokemon_attributes['pokemon_name'] = pokedex[pokemon_attributes['pokemon_id']]
        pokemon_attributes['IV'] = round((getattr(pokemon, 'individual_attack') +
                                         getattr(pokemon, 'individual_defense') +
                                         getattr(pokemon, 'individual_stamina')) * (100/45.0), 0)
        pokemon_attributes['image_nr'] = str(pokemon_attributes['pokemon_id']).zfill(3)
        pokemons.append(pokemon_attributes)

    return (pogo_session, sorted(pokemons, key=lambda k: k['IV'], reverse=True))


@app.route('/getpokemon', methods=['POST'])
def getpokemon():
    auth = request.json.get('auth', 'google')
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'error': 'need username and password'})

    # Check service
    if auth not in ['ptc', 'google']:
        logging.error('Invalid auth service {}'.format(auth))
        sys.exit(-1)

    session['username'] = username
    session['password'] = password
    session['auth'] = auth

    pogo_session, pokemons = get_pokemon(username, password, auth)
    #session['pogo_session'] = pogo_session

    return jsonify(pokemons)


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
