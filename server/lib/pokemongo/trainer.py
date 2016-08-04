#!/usr/bin/python
import argparse
import logging
import time
import sys
from custom_exceptions import GeneralPogoException

from api import PokeAuthSession
from location import Location
from inventory import items
import traceback

from pokedex import pokedex
from pogo.POGOProtos.Settings.Master.Item.PokeballAttributes_pb2 import PokeballAttributes


def save_coordinates_to_disk(coor, filename='coor.log'):
    with open(filename, 'w') as f:
        for coordinate in coor:
            f.write('{latitude},{longitude}\n'.format(latitude=coordinate.latitude, longitude=coordinate.longitude))

config = {}
config['locations'] = {

'water_locations': [
    'Den Bosch, Zuidwal 11',
    '51.683096, 5.302949',
    '51.684959, 5.301098',
    '51.683661, 5.296121',
    '51.679782, 5.294437',
    '51.682904, 5.293952',
    '51.681795, 5.289870',
    '51.687805, 5.293879',
    '51.691384, 5.299243',
    '51.694217, 5.299179',
    '51.702921, 5.290038',
],

'tilburg': ['51.560125, 5.083498',
           '51.559538, 5.091222',
           '51.562606, 5.091137',
           '51.567434, 5.088304',
           '51.567141, 5.081867',
           '51.563860, 5.083498',
           '51.560178, 5.078005',
           '51.556843, 5.077704',
           '51.552147, 5.080708',
           '51.557670, 5.081309',
           '51.558657, 5.087532',
           '51.556124, 5.091115',
           '51.553803, 5.089023',
           '51.552575, 5.092692',
           '51.552195, 5.094827',
           '51.552702, 5.097338',
           '51.555715, 5.096345',
           '51.558365, 5.094457',
           '51.560284, 5.081264',
           '51.556040, 5.088258',
           '51.555506, 5.085082',
           '51.553505, 5.081499',
           '51.552158, 5.080705',
           '51.551864, 5.076692',
           '51.550543, 5.071586',
           '51.552438, 5.069204',
           '51.554279, 5.067315',
           '51.557321, 5.068303',
           '51.561416, 5.074289',
           '51.563937, 5.073753',
           '51.565631, 5.077701',
           '51.563097, 5.080426',
           '51.561229, 5.079697',
           ],

'efteling': [
            '51.648820, 5.050254'
            ],

'denbosch_centrum': [
                    '51.683957, 5.296741',
                    '51.684356, 5.303350',
                    '51.678928, 5.301633',
                    '51.676932, 5.312920',
                    '51.672381, 5.315538',
                    '51.673818, 5.325751',
                    '51.677704, 5.320730',
                    '51.683185, 5.320602',
                    '51.685899, 5.312662',
                    '51.688081, 5.309401',
                    '51.688400, 5.315323',
                    '51.691539, 5.307985',
                    '51.693561, 5.299659',
                    '51.690289, 5.303157',
                    '51.688533, 5.303414',
                    '51.689012, 5.298522',
                    '51.687003, 5.300346',
                    '51.686179, 5.295496',
                    '51.686006, 5.290947',
                    '51.687110, 5.288565',
                    '51.686977, 5.285068',
                    '51.688972, 5.282579',
                    '51.691832, 5.282214',
                    '51.687322, 5.278116',
                    '51.686005, 5.278373',
                    '51.684017, 5.278341',
                    '51.684855, 5.272698',
                    '51.685786, 5.273148',
                    '51.687003, 5.276818',
                    '51.688879, 5.275090',
                    '51.688573, 5.277128',
                    '51.690382, 5.272751',
                    '51.693920, 5.276764',
                    '51.696900, 5.268781',
                    '51.697485, 5.260091',
                    '51.702778, 5.262666',
                    '51.704932, 5.267515',
                    '51.708934, 5.270820',
                    '51.704014, 5.280218',
                    '51.708855, 5.281742',
                    '51.708123, 5.293436',
                    '51.702485, 5.292342',
                    '51.702166, 5.306740',
                    '51.696713, 5.312491',
                    '51.693681, 5.317469',
                    '51.693175, 5.308306',
                    '51.692191, 5.314872',
                    '51.692683, 5.326953',
                    '51.696368, 5.324979',
                    '51.699440, 5.325623',
                    '51.701661, 5.330494',
                    '51.698349, 5.336094',
                    '51.696673, 5.339441',
                    '51.697618, 5.341523',
                    '51.692138, 5.339935',
                    '51.689637, 5.343776',
                    '51.687868, 5.338154',
                    '51.688453, 5.331631',
                    '51.691539, 5.332725',
                    '51.689784, 5.325215',
                    '51.685620, 5.324915',
                    '51.684702, 5.315645',
                    '51.685261, 5.309251',
                    '51.686524, 5.304873',
                    '51.686924, 5.300796',
                    '51.685499, 5.297152',
                    ],

'bijlmer': ['52.313873, 4.951974',
           '52.312925, 4.924999',
           '52.298204, 4.939119',
           '52.307218, 4.964653',
           '52.312935, 4.981653',
           '52.316280, 4.979121',
           '52.316745, 4.969101',
           '52.340654, 4.992044',
           '52.349149, 5.004146',
           '52.355597, 4.980886',
           '52.314502, 4.941578',
           ],

'zuiderplas': [
              '51.672547, 5.312482',
              '51.674729, 5.311774',
              '51.677204, 5.312976',
              '51.675621, 5.318319',
              '51.677909, 5.318469',
              '51.678002, 5.323812',
              '51.677714, 5.328566',
              '51.678105, 5.334394',
              '51.676092, 5.333203',
              '51.672882, 5.323460',
              '51.671574, 5.314402',
              ],

'zandvoort': ['52.342815, 4.503499',
             '52.333376, 4.497319',
             '52.322832, 4.489809',
             '52.311919, 4.481741',
             '52.322832, 4.489809',
             '52.333376, 4.497319',
             '52.342815, 4.503499',
             ],

'texel': ['52.998429, 4.766776',
         '53.000082, 4.738967',
         '53.011238, 4.735190',
         '53.019706, 4.719741',
         '53.032509, 4.710814',
         '53.049229, 4.716651',
         '53.068315, 4.725920',
         '53.094918, 4.748751',
         '53.131573, 4.788706',
         '53.146814, 4.818231',
         '53.167194, 4.825441',
         '53.183968, 4.846894',
         '53.158861, 4.875390',
         '53.136829, 4.905945',
         '53.116846, 4.897362',
         '53.101801, 4.894272',
         '53.077471, 4.892899',
         '53.056842, 4.871956',
         '53.032717, 4.829935',
         '53.006488, 4.783930',
         ],
'new_york': [''],
'dam': ['52.373180, 4.892041'],
}

# CONSTANTS
SEARCH_POKEMON = 1
SEARCH_STOPS = 2
POKEBALL = 1
GREATBALL = 2
ULTRABALL = 3

# options
MAX_EMPTY_SEARCHES = 1
BLACKLIST = []  #[69, 90, 98, 116, 118, 120, 72, 79, 81, 86, 92, 96, 129]
WHITELIST = [2, 3, 4, 5, 6, 8, 9, 25, 26, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 58, 59]
MIN_ID = None
PB_API = None
PB_DEV = None

config['options'] = {'blacklist': [],
                     'whitelist': [2, 3, 4, 5, 6, 8, 9, 25, 26, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 58, 59],
                     'evolvables': [
            pokedex.PIDGEY, pokedex.RATTATA, pokedex.ZUBAT, pokedex.ODDISH, pokedex.WEEDLE, pokedex.CATERPIE,
            pokedex.STARYU, pokedex.GOLDEEN, pokedex.ODDISH, pokedex.KAKUNA
        ],
        'throw_aways': [
            pokedex.PIDGEY, pokedex.RATTATA, pokedex.ZUBAT, pokedex.ODDISH, pokedex.WEEDLE, pokedex.PSYDUCK,
            pokedex.CATERPIE, pokedex.DROWZEE, pokedex.VENONAT, pokedex.PIDGEOTTO, pokedex.MAGIKARP, pokedex.EEVEE,
            pokedex.KAKUNA, pokedex.ODDISH, pokedex.KAKUNA, pokedex.POLIWAG, pokedex.EXEGGCUTE, pokedex.RATICATE,
            pokedex.METAPOD
        ],
        'min_id': None,
        'max_empty_searches': 1,  # Can use this to search multiple time on the same location
        'max_items_in_bag': {1: 80, 2: 100, 3: 100, 101: 0, 102: 0, 103: 50, 201: 25, 301: 25, 401: 0, 501: 0, 701: 20}
                     }

config['params'] = {'action': 'stop',
                    'username': '',
                    'password': '',
                    'auth': 'google',
                    'pb_api': '',
                    'pb_dev': '',
                    'geo_key': '',
                    'location': 'dam',  # Specify the config['locations']['key'] key.
                    }

search_mode = config['params']['search_mode']
search_locations = config['locations']['dam']

last_search_location_index = 0
location_tracker = []


class Tracker(dict):
    stop_spinned = 0
    pokemon_caucht = 1

    def __init__(self, ts, location, action=None, points_scored=0, pokemon_caucht=None):
        self.ts = ts
        self.location = location
        self.points_scored = 0
        self.pokemon_caucht = 0


def setupLogger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('Line %(lineno)d,%(filename)s - %(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)


class Trainer(object):
    def __init__(self, session, config):
        self.session = session
        self.config = config

    @staticmethod
    def get_nex_location():
        global last_search_location_index
        if last_search_location_index + 1 > len(search_locations) - 1:
            last_search_location_index = 0
        last_search_location_index += 1
        return search_locations[last_search_location_index]

    # Example functions
    # Get profile
    def getProfile(self):
        logging.info("Printing Profile:")
        profile = self.session.getProfile()
        logging.info(profile)

    def sortClosePokemon(self, minimum_id=None, blacklist=[], whitelist=[]):
        """Get Map details and print pokemon"""

        ordered_pokemons = []
        cells = self.session.getMapObjects(radius=20)

        latitude, longitude, _ = self.session.getCoordinates()
        logging.info("Searching for pokemon, from position: %s, %s", self.session.location.latitude, self.session.location.longitude)

        for cell in cells.map_cells:
            # Heap in pokemon protos where we have long + lat
            pokemons = [p for p in cell.wild_pokemons]
            for pokemon in pokemons:
                # Log the pokemon found
                pokemon_id = getattr(pokemon, "pokemon_id", None)
                if not pokemon_id:
                    pokemon_id = pokemon.pokemon_data.pokemon_id

                if minimum_id:
                    if pokemon_id < minimum_id:
                        logging.debug('Ignoring pokemon {0} with id {1}, because its below {2}'.format(pokedex[pokemon_id],
                                                                                                       pokemon_id,
                                                                                                       minimum_id))
                        continue

                if pokemon_id in blacklist and pokemon_id not in whitelist:
                    logging.info('Ignoring pokemon {0} with id {1}, because its blacklisted'.format(pokedex[pokemon_id],
                                                                                                    pokemon_id))
                    continue

                rarity = pokedex.getRarityById(pokemon_id)

                # Fins distance to pokemon
                dist = Location.getDistance(
                    latitude,
                    longitude,
                    pokemon.latitude,
                    pokemon.longitude
                )

                # Log the pokemon found
                logging.info("%s, %f meters away" % (
                    pokedex[pokemon_id],
                    dist
                ))

                ordered_pokemons.append({'distance': dist, 'pokemon': pokemon})

        # Remove visited forts if provided
        ordered_pokemons = sorted(ordered_pokemons, key=lambda k: k['distance'])
        return [instance['pokemon'] for instance in ordered_pokemons]

    # Wrap both for ease
    def encounterAndCatch(self, pokemon, thresholdP=0.5, limit=5, delay=2):
        # Start encounter
        encounter = self.session.encounterPokemon(pokemon)

        # Grab needed data from proto
        chances = encounter.capture_probability.capture_probability
        balls = encounter.capture_probability.pokeball_type
        bag = self.session.checkInventory().bag

        # Have we used a razz berry yet?
        berried = False

        # Make sure we aren't oer limit
        count = 0

        # Attempt catch
        while True:
            bestBall = items.UNKNOWN
            altBall = items.UNKNOWN

            # Check for balls and see if we pass
            # wanted threshold
            for i, ball in enumerate(balls):
                if bag.get(ball, 0) > 0:
                    altBall = ball
                    if chances[i] > thresholdP:
                        bestBall = ball
                        break

            # If we can't determine a ball, try a berry
            # or use a lower class ball
            if bestBall == items.UNKNOWN:
                if not berried and bag.get(items.RAZZ_BERRY, 0) > 0:
                    logging.info('Using a RAZZ_BERRY')
                    self.session.useItemCapture(items.RAZZ_BERRY, pokemon)
                    berried = True
                    time.sleep(delay)
                    continue

                # if no alt ball, there are no balls
                elif altBall == items.UNKNOWN:
                    raise GeneralPogoException('Out of usable balls')
                else:
                    bestBall = altBall

            # Try to catch it!!
            logging.info('Using a %s' % items[bestBall])
            attempt = self.session.catchPokemon(pokemon, bestBall)
            time.sleep(delay)

            # Success or run away
            if attempt.status == 1:
                return attempt

            # CATCH_FLEE is bad news
            if attempt.status == 3:
                logging.info('Possible soft ban.')
                return attempt

            # Only try up to x attempts
            count += 1
            if count >= limit:
                logging.info('Over catch limit')
                return None

    def findClosestPokemon(self):
        """Grab the nearest pokemon details"""
        logging.info('Finding Nearest Fort:')
        return self.sortClosePokemon()[0]

    # Catch a pokemon at a given point
    def walkAndCatch(self, pokemon, pokeball=None):
        if pokemon:
            pokemon_id = getattr(pokemon, 'pokemon_id', None)
            if not pokemon_id:
                pokemon_id = pokemon.pokemon_data.pokemon_id

            logging.info('Catching %s:', pokedex[pokemon_id])

            rarity = pokedex.getRarityById(pokemon_id)

            logging.info('Catching %s:' % pokedex[pokemon_id])
            self.session.walkTo(pokemon.latitude, pokemon.longitude, step=4.5)

            attempt = self.encounterAndCatch(pokemon)
            if attempt and attempt.status == 1:
                if all([self.session.pushbullet,
                        self.session.pushbullet.pushbullet_device]):
                            self.session.pushbullet.notify_pokemon(pokemon,
                                                                   poke_name=pokedex[pokemon_id])
                self.cleanPokemon(thresholdCP=100)

            logging.info(attempt)

    # Do Inventory stuff
    def getInventory(self):
        logging.info('Get Inventory:')
        logging.info(self.session.getInventory())

    # Basic solution to spinning all forts.
    # Since traveling salesman problem, not
    # true solution. But at least you get
    # those step in
    def sortCloseForts(self, visited=[]):
        # Sort nearest forts (pokestop)
        logging.info('Sorting Nearest Forts:')
        cells = self.session.getMapObjects()
        latitude, longitude, _ = self.session.getCoordinates()
        ordered_forts = []
        for cell in cells.map_cells:
            for fort in cell.forts:
                dist = Location.getDistance(
                    latitude,
                    longitude,
                    fort.latitude,
                    fort.longitude
                )
                if fort.type == 1 and fort.cooldown_complete_timestamp_ms<time.time():
                    ordered_forts.append({'distance': dist, 'fort': fort})

        # Remove visited forts if provided
        ordered_forts = [fort for fort in ordered_forts if fort['fort'].id not in visited]
        ordered_forts = sorted(ordered_forts, key=lambda k: k['distance'])
        return [instance['fort'] for instance in ordered_forts]

    # Find the fort closest to user
    def findClosestFort(self):
        # Find nearest fort (pokestop)
        logging.info('Finding Nearest Fort:')
        return self.sortCloseForts()[0]

    # Walk to fort and spin
    def walkAndSpin(self, fort):
        # No fort, demo == over
        if fort:
            logging.info('Spinning a Fort:')
            # Walk over
            self.session.walkTo(fort.latitude, fort.longitude, step=4, search_each=15,
                                walk_and_catch_callback=self.search_pokemon)

            self.purge_items()
            self.setEgg()

            # Give it a spin
            fortResponse = self.session.getFortSearch(fort)
            # Change my current location to the pokemons location
            self.session.setCoordinates(fort.latitude, fort.longitude)
            logging.info(fortResponse)

    def purge_items(self):
        """ Configuration of the maximum number of items you want to keep caried 
        1: pokeball
        2: great ball
        3: ultra ball
        101: potion
        102: super potion
        103: hyper potion
        201: Revive
        301: ?
        401: incense
        501: lure module
        """
        max_items = self.config['options']['max_items_in_bag']
        bag = self.session.getInventory().bag

        for item_id, max_count in max_items.items():
            if bag[item_id] > max_count:
                logging.debug('Deleting for item_id: %s, count: %s', bag[item_id], bag[item_id] - max_count)
                self.session.recycleItem(item_id, bag[item_id] - max_count)

    # Walk and spin everywhere
    def walkAndSpinMany(self, forts):
        for fort in forts:
            self.walkAndSpin(fort)

    # A very brute force approach to evolving
    def evolveAllPokemon(self):
        inventory = self.session.checkInventory()
        for pokemon in inventory["party"]:
            logging.info(self.session.evolvePokemon(pokemon))
            time.sleep(1)

    # You probably don't want to run this
    def releaseAllPokemon(self):
        inventory = self.session.checkInventory()
        for pokemon in inventory["party"]:
            self.session.releasePokemon(pokemon)
            time.sleep(1)

    # Just incase you didn't want any revives
    def tossRevives(self):
        bag = self.session.checkInventory()["bag"]

        # 201 are revives.
        # TODO: We should have a reverse lookup here
        return self.session.recycleItem(201, bag[201])

    # Set an egg to an incubator
    def setEgg(self):
        inventory = self.session.checkInventory()

        # If no eggs, nothing we can do
        if len(inventory.eggs) == 0:
            return None

        egg = inventory.eggs[0]
        incubator = inventory.incubators[0]
        return self.session.setEgg(incubator, egg)

    # Understand this function before you run it.
    # Otherwise you may flush pokemon you wanted.
    def cleanPokemon(self, thresholdCP=50):
        logging.info("Cleaning out Pokemon...")
        party = self.session.checkInventory().party

        evolables = self.config['options']['evolvables']

        throw_aways = self.config['options']['throw_aways']

        toEvolve = {evolve: [] for evolve in evolables}

        for pokemon in party:
            # Get the highest CP value for this pokemon
            cps = [pok.cp for pok in party if pok.pokemon_id == pokemon.pokemon_id]

            # If there are already multiple of this pokemon available, and the cp for this pokemon is lower, throw away
            if pokemon.pokemon_id in throw_aways and len(cps) > 1 and pokemon.cp < max(cps):
                self.session.releasePokemon(pokemon)
                continue

            if pokemon.pokemon_id in evolables and len(cps) == 1 and pokemon.cp == max(cps):
                toEvolve[pokemon.pokemon_id].append(pokemon)
                continue

        # Evolve those we want
        for evolve in evolables:
            # if we don't have any candies of that type e.g. not caught that pokemon yet
            if evolve not in self.session.checkInventory().candies:
                continue
            candies = self.session.checkInventory().candies[evolve]
            pokemons = toEvolve[evolve]
            # release for optimal candies
            while candies // pokedex.evolves[evolve] < len(pokemons):
                pokemon = pokemons.pop()
                logging.info("Releasing %s" % pokedex[pokemon.pokemon_id])
                self.session.releasePokemon(pokemon)
                time.sleep(1)
                candies += 1

            # evolve remainder
            for pokemon in pokemons:
                logging.info("Evolving %s" % pokedex[pokemon.pokemon_id])
                logging.info(self.session.evolvePokemon(pokemon))
                time.sleep(1)
                self.session.releasePokemon(pokemon)
                time.sleep(1)

    def botTheStops(self):
        # Trying not to flood the servers
        cooldown = 1

        stop = False
        while not stop:
            visited_stops = []
            try:
                forts = self.sortCloseForts(visited=visited_stops)
                save_coordinates_to_disk(forts)
                logging.info("Detected %s forts, going to spin first 10", len(forts))
                for fort in forts[:100]:
                    self.walkAndSpin(fort)
                    logging.info("Search for pokemon at the stop")
                    self.search_pokemon()
                    visited_stops.append(fort.id)
                    forts = self.sortCloseForts(visited=visited_stops)
                    time.sleep(1)
            except Exception:
                logging.critical("Exception detected! [%s], trying to continue!", traceback.format_exc())
                start_location = self.config['locations'][config['params']['location']][0]
                session = poko_session.authenticate(start_location)
                session.setup_pushbullet(self.config['params']['pb_api'],
                                         self.config['params']['pb_dev'])
                time.sleep(cooldown)
                cooldown *= 2
                if cooldown == 64:
                    raise
                continue

    def search_pokemon(self):
        inventory = session.getInventory()
        # stop for now, when we have 250 pokemon
        if len(inventory.party) >= 250:
            logging.error('Pokemon Inventory full (250), cant catch this one')
            time.sleep(2)
            return None

        sorted_list_of_pokemon = self.sortClosePokemon(minimum_id=self.config['options']['min_id'],
                                                       blacklist=self.config['options']['blacklist'],
                                                       whitelist=self.config['options']['whitelist'])

        for pokemon in sorted_list_of_pokemon:
            self.walkAndCatch(pokemon)

    def botThePokemon(self):
        # Trying not to flood the servers
        cooldown = 1
        global search_locations

        # Use stops as coordinates to look for pokemon
        if len(search_locations) < 5:
            search_locations = ['{0}, {1}'.format(fort.latitude, fort.longitude) for fort in self.sortCloseForts()]

        # Pokemon related
        empty_searches = 0
        stop = False
        while not stop:
            try:
                inventory = session.getInventory()
                # stop for now, when we have 250 pokemon
                if len(inventory.party) >= 250:
                    stop = True

                # Use greatballs if all your pokeballs have been used
                # Then if greatballs are used, bot the stops
                if inventory.bag[1] == 0 and inventory.bag[2] == 0:
                    self.botTheStops()

                # When we haven't found a pokemon for 10 searches in a row, let's move on
                if empty_searches >= self.config['options']['max_empty_searches']:
                    self.changeLocation(self.get_nex_location())
                    empty_searches = 0
                    continue

                sorted_list_of_pokemon = self.sortClosePokemon(minimum_id=self.config['options']['min_id'],
                                                               blacklist=self.config['options']['blacklist'],
                                                               whitelist=self.config['options']['whitelist'])
                if not sorted_list_of_pokemon:
                    empty_searches += 1

                for pokemon in sorted_list_of_pokemon:
                    self.walkAndCatch(pokemon)
                    empty_searches = 0
                    time.sleep(3)

                time.sleep(2)
            except Exception:
                logging.critical("Exception detected! [%s], trying to continue!", traceback.format_exc())
                session = poko_session.reauthenticate(session)
                session.setup_pushbullet(self.config['params']['pb_api'],
                                         self.config['params']['pb_dev'])
                time.sleep(cooldown)
                cooldown *= 2
                if cooldown == 64:
                    raise
                continue

    def changeLocation(self, maps_location, geo_key=None):
        latitude, longitude = [float(loc) for loc in maps_location.split(', ')]
        self.session.setCoordinates(latitude, longitude)
        logging.info("Continue to search on location: %s", maps_location)

# Entry point
# Start off authentication and demo
if __name__ == '__main__':
    setupLogger()
    logging.debug('Logger set up')

    # Read in args
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--auth", help="Auth Service", required=True)
    parser.add_argument("-u", "--username", help="Username", required=True)
    parser.add_argument("-p", "--password", help="Password", required=True)
    parser.add_argument("-l", "--location", help="Location", required=True)
    parser.add_argument("-c", "--action", help="Action", required=False)
    parser.add_argument("-x", "--pb_api", help="Pushbullet Api key", required=False)
    parser.add_argument("-y", "--pb_dev", help="Pushbullet Device key", required=False)
    parser.add_argument("-g", "--geo_key", help="GEO API Secret")
    args = parser.parse_args()

    config['params']['auth'] = args.auth or config['params']['auth']
    config['params']['username'] = args.username or config['params']['username']
    config['params']['password'] = args.password or config['params']['password']
    config['params']['location'] = args.location or config['params']['location']
    config['params']['pb_api'] = args.pb_api or config['params']['pb_api']
    config['params']['pb_dev'] = args.pb_dev or config['params']['pb_dev']
    config['params']['geo_key'] = args.geo_key or config['params']['geo_key']
    config['params']['action'] = args.action or config['params']['action']

    # Check service
    if args.auth not in ['ptc', 'google']:
        logging.error('Invalid auth service {}'.format(args.auth))
        sys.exit(-1)

    if 'stop' in args.action.lower():
        config['params']['search_mode'] = SEARCH_STOPS
    if 'pokemon' in args.action.lower():
        config['params']['search_mode'] = SEARCH_POKEMON

    # Create PokoAuthObject
    poko_session = PokeAuthSession(
        config['params']['username'],
        config['params']['password'],
        config['params']['auth'],
        geo_key=config['params']['geo_key']
    )

    # Authenticate with a given location
    # Location is not inherent in authentication
    # But is important to session
    # session = poko_session.authenticate(args.location)
    start_location = config['locations'][config['params']['location']][0]
    session = poko_session.authenticate(locationLookup=start_location)
    if config['params']['pb_api']:
        PB_API = config['params']['pb_api']
        PB_DEV = config['params']['pb_dev']
        session.setup_pushbullet(PB_API, PB_DEV)

    # Time to show off what we can do
    if session:
        trainer = Trainer(session)

        # General
        trainer.session.getProfile()
        trainer.session.getInventory()

        try:
            if search_mode == SEARCH_POKEMON:
                trainer.botThePokemon(config)

            elif search_mode == SEARCH_STOPS:
                # Pokestop related
                # Keep track of stops we just visited
                trainer.botTheStops(config)
        except Exception as e:
            if all([session.pushbullet,
                   trainer.session.pushbullet.pushbullet_device]):
                trainer.session.pushbullet.notify_pokemon('Bot stopped!', 'Exception: {0}'.format(e))

    else:
        logging.critical('Session not created successfully')
