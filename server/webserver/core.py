# coding=utf-8

from __future__ import unicode_literals

import json
import logging
import time
from requests.exceptions import ConnectionError, HTTPError

from pokemongo.api import PokeAuthSession
from pokemongo.location import Location
from pokemongo.pokedex import pokedex, move_list
from pokemongo.custom_exceptions import GeneralPogoException

import tornado
from tornado.web import RequestHandler

store = {}


class BaseHandler(RequestHandler):
    def initialize(self, store):
        self.store = store

    def get_username(self):
        return self.get_secure_cookie('username')

    def set_username(self, some_value):
        return self.set_secure_cookie('username', some_value)

    def get_password(self):
        return self.get_secure_cookie('password')

    def set_password(self, some_value):
        return self.set_secure_cookie('password', some_value)

    def get_auth(self):
        return self.get_secure_cookie('auth')

    def set_auth(self, some_value):
        return self.set_secure_cookie('auth', some_value)

    def get_access_token(self):
        return self.get_secure_cookie('access_token')

    def set_access_token(self, some_value):
        return self.set_secure_cookie('access_token', some_value)

    def get_pokemon(self):
        pogo_session = self.check_refresh_session()

#         if not pogo_session:
#             return redirect(url_for('openApp'))

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
            return {'pokemons': sorted(pokemons, key=lambda k: k['IV'], reverse=True)}
        return []

    def get_pogo_auth(self, username=None, password=None, auth='google'):
        # Create PokoAuthObject

        if (not username or not password) and not self.store.get(self.get_username()):
            raise tornado.web.HTTPError(401)

        if username and password:
            # Create a new session
            auth = PokeAuthSession(
                username,
                password,
                auth,
            )
            pogo_session = auth.authenticate()
            self.store[username] = {'session': pogo_session, 'last_update': time.time()}
        else:
            # reuse old
            pogo_session = self.store[self.get_username()].get('session')

        return pogo_session

    def check_refresh_session(self, timeout=1800):
        username = self.get_username()
        password = self.get_password()
        auth = self.get_auth()

        if (username and
            self.store.get(username) and
                self.store[username].get('last_update') + timeout < time.time()):
            return self.get_pogo_auth(username, password, auth)
        else:
            return self.get_pogo_auth()


class JsonHandler(BaseHandler):
    """Request handler where requests and responses speak JSON."""
    def prepare(self):
        # Incorporate request JSON into arguments dictionary.
        if self.request.body:
            try:
                json_data = json.loads(self.request.body)
                self.request.arguments.update(json_data)
            except ValueError:
                message = 'Unable to parse JSON.'
                self.send_error(400, message=message) # Bad Request

        # Set up response dictionary.
        self.response = dict()

    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json')

    def write_error(self, status_code, **kwargs):
        if 'message' not in kwargs:
            if status_code == 405:
                kwargs['message'] = 'Invalid HTTP method.'
            else:
                kwargs['message'] = 'Unknown error.'

        self.response = kwargs
        self.write_json()

    def write_json(self):
        output = json.dumps(self.response)
        self.write(output)


class HomeHandler(BaseHandler):
    def get(self):
        self.render("index.html")


class LoginHandler(JsonHandler):
    def post(self):
        error = False
        error_msg = ''
        data = tornado.escape.json_decode(self.request.body)
        username = data.get('username')
        password = data.get('password')
        auth = data.get('auth')

        if not username or not password:
            self.response = {'error': 'need username and password'}
            self.write_json()

        # Check service
        if auth not in ['ptc', 'google']:
            self.response = {'error': 'Invalid auth service {0}'.format(auth)}
            self.write_json()

        self.set_secure_cookie('username', username)
        self.set_secure_cookie('password', password)
        self.set_secure_cookie('auth', auth)

        try:
            pogo_session = self.get_pogo_auth(username, password, auth)
            access_token = pogo_session.accessToken
        except (ConnectionError, HTTPError, GeneralPogoException) as e:
            error = True
            error_msg = e
            pogo_session = None
            access_token = ''

        if pogo_session:
            self.store[username]['access_token'] = {'last_update': time.time(), 'token': pogo_session.accessToken}

        self.response = {'authenticated': bool(pogo_session), 'accessToken': access_token,
                         'error': error, 'error_msg': str(getattr(error_msg, 'message', ''))}

        self.write_json()


class PokemonHandler(JsonHandler):
    def get(self):

        pogo_session = self.check_refresh_session()

        if not pogo_session:
            self.response = {'error': 'Need to login first'}

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
            self.response = {'pokemons': sorted(pokemons, key=lambda k: k['IV'], reverse=True)}
            self.write_json()