import inspect


class Pokedex(dict):

    # Enum pokemonIds
    MISSINGNO = 0
    BULBASAUR = 1
    IVYSAUR = 2
    VENUSAUR = 3
    CHARMANDER = 4
    CHARMELEON = 5
    CHARIZARD = 6
    SQUIRTLE = 7
    WARTORTLE = 8
    BLASTOISE = 9
    CATERPIE = 10
    METAPOD = 11
    BUTTERFREE = 12
    WEEDLE = 13
    KAKUNA = 14
    BEEDRILL = 15
    PIDGEY = 16
    PIDGEOTTO = 17
    PIDGEOT = 18
    RATTATA = 19
    RATICATE = 20
    SPEAROW = 21
    FEAROW = 22
    EKANS = 23
    ARBOK = 24
    PIKACHU = 25
    RAICHU = 26
    SANDSHREW = 27
    SANDSLASH = 28
    NIDORAN_FEMALE = 29
    NIDORINA = 30
    NIDOQUEEN = 31
    NIDORAN_MALE = 32
    NIDORINO = 33
    NIDOKING = 34
    CLEFAIRY = 35
    CLEFABLE = 36
    VULPIX = 37
    NINETALES = 38
    JIGGLYPUFF = 39
    WIGGLYTUFF = 40
    ZUBAT = 41
    GOLBAT = 42
    ODDISH = 43
    GLOOM = 44
    VILEPLUME = 45
    PARAS = 46
    PARASECT = 47
    VENONAT = 48
    VENOMOTH = 49
    DIGLETT = 50
    DUGTRIO = 51
    MEOWTH = 52
    PERSIAN = 53
    PSYDUCK = 54
    GOLDUCK = 55
    MANKEY = 56
    PRIMEAPE = 57
    GROWLITHE = 58
    ARCANINE = 59
    POLIWAG = 60
    POLIWHIRL = 61
    POLIWRATH = 62
    ABRA = 63
    KADABRA = 64
    ALAKAZAM = 65
    MACHOP = 66
    MACHOKE = 67
    MACHAMP = 68
    BELLSPROUT = 69
    WEEPINBELL = 70
    VICTREEBEL = 71
    TENTACOOL = 72
    TENTACRUEL = 73
    GEODUDE = 74
    GRAVELER = 75
    GOLEM = 76
    PONYTA = 77
    RAPIDASH = 78
    SLOWPOKE = 79
    SLOWBRO = 80
    MAGNEMITE = 81
    MAGNETON = 82
    FARFETCHD = 83
    DODUO = 84
    DODRIO = 85
    SEEL = 86
    DEWGONG = 87
    GRIMER = 88
    MUK = 89
    SHELLDER = 90
    CLOYSTER = 91
    GASTLY = 92
    HAUNTER = 93
    GENGAR = 94
    ONIX = 95
    DROWZEE = 96
    HYPNO = 97
    KRABBY = 98
    KINGLER = 99
    VOLTORB = 100
    ELECTRODE = 101
    EXEGGCUTE = 102
    EXEGGUTOR = 103
    CUBONE = 104
    MAROWAK = 105
    HITMONLEE = 106
    HITMONCHAN = 107
    LICKITUNG = 108
    KOFFING = 109
    WEEZING = 110
    RHYHORN = 111
    RHYDON = 112
    CHANSEY = 113
    TANGELA = 114
    KANGASKHAN = 115
    HORSEA = 116
    SEADRA = 117
    GOLDEEN = 118
    SEAKING = 119
    STARYU = 120
    STARMIE = 121
    MR_MIME = 122
    SCYTHER = 123
    JYNX = 124
    ELECTABUZZ = 125
    MAGMAR = 126
    PINSIR = 127
    TAUROS = 128
    MAGIKARP = 129
    GYARADOS = 130
    LAPRAS = 131
    DITTO = 132
    EEVEE = 133
    VAPOREON = 134
    JOLTEON = 135
    FLAREON = 136
    PORYGON = 137
    OMANYTE = 138
    OMASTAR = 139
    KABUTO = 140
    KABUTOPS = 141
    AERODACTYL = 142
    SNORLAX = 143
    ARTICUNO = 144
    ZAPDOS = 145
    MOLTRES = 146
    DRATINI = 147
    DRAGONAIR = 148
    DRAGONITE = 149
    MEWTWO = 150
    MEW = 151

    rarity = {}
    evolves = {}

    def __init__(self):
        super(dict, self).__init__(self)

        # Some reflection, based on uppercase consts.
        attributes = inspect.getmembers(Pokedex, lambda attr: not(inspect.isroutine(attr)))
        for attr in attributes:
            if attr[0].isupper():
                self[attr[1]] = attr[0]

        # Ideally go back and lint for line lengths
        self.rarity[Rarity.MYTHIC] = [self.MEW]
        self.rarity[Rarity.LEGENDARY] = [
            self.ZAPDOS, self.MOLTRES, self.MEWTWO, self.ARTICUNO
        ]
        self.rarity[Rarity.EPIC] = [
            self.DITTO, self.VENUSAUR, self.TAUROS, self.DRAGONITE, self.CLEFABLE,
            self.CHARIZARD, self.BLASTOISE
        ]
        self.rarity[Rarity.VERY_RARE] = [
            self.WEEPINBELL, self.WARTORTLE, self.VILEPLUME, self.VICTREEBEL,
            self.VENOMOTH, self.VAPOREON, self.SLOWBRO, self.RAICHU, self.POLIWRATH,
            self.PINSIR, self.PIDGEOT, self.OMASTAR, self.NIDOQUEEN, self.NIDOKING,
            self.MUK, self.MAROWAK, self.LAPRAS, self.KANGASKHAN, self.KABUTOPS, self.IVYSAUR,
            self.GYARADOS, self.GOLEM, self.GENGAR, self.EXEGGUTOR, self.DRAGONAIR, self.DEWGONG,
            self.CHARMELEON, self.BEEDRILL, self.ALAKAZAM
        ]
        self.rarity[Rarity.RARE] = [
            self.WIGGLYTUFF, self.WEEZING, self.TENTACRUEL, self.TANGELA,
            self.STARMIE, self.SNORLAX, self.SCYTHER, self.SEAKING, self.SEADRA,
            self.RHYDON, self.RAPIDASH, self.PRIMEAPE, self.PORYGON, self.POLIWHIRL,
            self.PARASECT, self.ONIX, self.OMANYTE, self.NINETALES, self.NIDORINO,
            self.NIDORINA, self.MR_MIME, self.MAGMAR, self.MACHOKE, self.MACHAMP,
            self.LICKITUNG, self.KINGLER, self.JOLTEON, self.HYPNO, self.HITMONCHAN,
            self.GLOOM, self.GOLDUCK, self.FLAREON, self.FEAROW, self.FARFETCHD,
            self.ELECTABUZZ, self.DUGTRIO, self.DRATINI, self.DODRIO, self.CLOYSTER,
            self.CHANSEY, self.BUTTERFREE, self.ARCANINE, self.AERODACTYL
        ]
        self.rarity[Rarity.UNCOMMON] = [
            self.VULPIX, self.TENTACOOL, self.STARYU, self.SQUIRTLE, self.SPEAROW,
            self.SHELLDER, self.SEEL, self.SANDSLASH, self.RHYHORN, self.RATICATE,
            self.PSYDUCK, self.PONYTA, self.PIKACHU, self.PIDGEOTTO, self.PERSIAN,
            self.METAPOD, self.MAGNETON, self.KOFFING, self.KADABRA, self.KABUTO,
            self.KAKUNA, self.JYNX, self.JIGGLYPUFF, self.HORSEA, self.HITMONLEE,
            self.HAUNTER, self.GROWLITHE, self.GRIMER, self.GRAVELER, self.GOLBAT,
            self.EXEGGCUTE, self.ELECTRODE, self.CUBONE, self.CLEFAIRY, self.CHARMANDER,
            self.BULBASAUR, self.ARBOK, self.ABRA
        ]
        self.rarity[Rarity.COMMON] = [
            self.WEEDLE, self.VOLTORB, self.VENONAT, self.SLOWPOKE, self.SANDSHREW,
            self.POLIWAG, self.PARAS, self.ODDISH, self.NIDORAN_MALE, self.NIDORAN_FEMALE,
            self.MEOWTH, self.MANKEY, self.MAGNEMITE, self.MAGIKARP, self.MACHOP, self.KRABBY,
            self.GOLDEEN, self.GEODUDE, self.GASTLY, self.EEVEE, self.EKANS, self.DROWZEE,
            self.DODUO, self.DIGLETT, self.CATERPIE, self.BELLSPROUT
        ]
        self.rarity[Rarity.CRITTER] = [self.ZUBAT, self.PIDGEY, self.RATTATA]

        self.evolves = {
            self.MISSINGNO: 0, self.BULBASAUR: 25, self.IVYSAUR: 100, self.VENUSAUR: 0,
            self.CHARMANDER: 25, self.CHARMELEON: 100, self.CHARIZARD: 0, self.SQUIRTLE: 25,
            self.WARTORTLE: 100, self.BLASTOISE: 0, self.CATERPIE: 12, self.METAPOD: 50,
            self.BUTTERFREE: 0, self.WEEDLE: 12, self.KAKUNA: 50, self.BEEDRILL: 0, self.PIDGEY: 12,
            self.PIDGEOTTO: 50, self.PIDGEOT: 0, self.RATTATA: 25, self.RATICATE: 0, self.SPEAROW: 50,
            self.FEAROW: 0, self.EKANS: 50, self.ARBOK: 0, self.PIKACHU: 50, self.RAICHU: 0,
            self.SANDSHREW: 50, self.SANDSLASH: 0, self.NIDORAN_FEMALE: 25, self.NIDORINA: 100,
            self.NIDOQUEEN: 0, self.NIDORAN_MALE: 25, self.NIDORINO: 100, self.NIDOKING: 0,
            self.CLEFAIRY: 50, self.CLEFABLE: 0, self.VULPIX: 50, self.NINETALES: 0, self.JIGGLYPUFF: 50,
            self.WIGGLYTUFF: 0, self.ZUBAT: 50, self.GOLBAT: 0, self.ODDISH: 25, self.GLOOM: 100,
            self.VILEPLUME: 0, self.PARAS: 50, self.PARASECT: 0, self.VENONAT: 50, self.VENOMOTH: 0,
            self.DIGLETT: 50, self.DUGTRIO: 0, self.MEOWTH: 50, self.PERSIAN: 0, self.PSYDUCK: 50,
            self.GOLDUCK: 0, self.MANKEY: 50, self.PRIMEAPE: 0, self.GROWLITHE: 50, self.ARCANINE: 0,
            self.POLIWAG: 25, self.POLIWHIRL: 100, self.POLIWRATH: 0, self.ABRA: 25, self.KADABRA: 100,
            self.ALAKAZAM: 0, self.MACHOP: 25, self.MACHOKE: 100, self.MACHAMP: 0, self.BELLSPROUT: 25,
            self.WEEPINBELL: 100, self.VICTREEBEL: 0, self.TENTACOOL: 50, self.TENTACRUEL: 0,
            self.GEODUDE: 25, self.GRAVELER: 100, self.GOLEM: 0, self.PONYTA: 50, self.RAPIDASH: 0,
            self.SLOWPOKE: 50, self.SLOWBRO: 0, self.MAGNEMITE: 50, self.MAGNETON: 0, self.FARFETCHD: 0,
            self.DODUO: 50, self.DODRIO: 0, self.SEEL: 50, self.DEWGONG: 0, self.GRIMER: 50, self.MUK: 0,
            self.SHELLDER: 50, self.CLOYSTER: 0, self.GASTLY: 25, self.HAUNTER: 100, self.GENGAR: 0,
            self.ONIX: 0, self.DROWZEE: 50, self.HYPNO: 0, self.KRABBY: 50, self.KINGLER: 0, self.VOLTORB: 50,
            self.ELECTRODE: 0, self.EXEGGCUTE: 50, self.EXEGGUTOR: 0, self.CUBONE: 50, self.MAROWAK: 0,
            self.HITMONLEE: 0, self.HITMONCHAN: 0, self.LICKITUNG: 0, self.KOFFING: 50, self.WEEZING: 0,
            self.RHYHORN: 50, self.RHYDON: 0, self.CHANSEY: 0, self.TANGELA: 0, self.KANGASKHAN: 0,
            self.HORSEA: 50, self.SEADRA: 0, self.GOLDEEN: 50, self.SEAKING: 0, self.STARYU: 50, self.STARMIE: 0,
            self.MR_MIME: 0, self.SCYTHER: 0, self.JYNX: 0, self.ELECTABUZZ: 0, self.MAGMAR: 0, self.PINSIR: 0,
            self.TAUROS: 0, self.MAGIKARP: 400, self.GYARADOS: 0, self.LAPRAS: 0, self.DITTO: 0, self.EEVEE: 25,
            self.VAPOREON: 0, self.JOLTEON: 0, self.FLAREON: 0, self.PORYGON: 0, self.OMANYTE: 50, self.OMASTAR: 0,
            self.KABUTO: 50, self.KABUTOPS: 0, self.AERODACTYL: 0, self.SNORLAX: 0, self.ARTICUNO: 0,
            self.ZAPDOS: 0, self.MOLTRES: 0, self.DRATINI: 25, self.DRAGONAIR: 100, self.DRAGONITE: 0,
            self.MEWTWO: 0, self.MEW: 0
        }

    def getRarityByName(self, name):
        return self.RarityById(self[name])

    def getRarityById(self, pokemonId):
        for rarity in self.rarity:
            if pokemonId in self.rarity[rarity]:
                return rarity


class Rarity(object):
    CRITTER = 0
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    VERY_RARE = 4
    EPIC = 5
    LEGENDARY = 6
    MYTHIC = 7


move_list = {0: 'MOVE_UNSET', 1: 'THUNDER_SHOCK', 2: 'QUICK_ATTACK', 3: 'SCRATCH', 4: 'EMBER', 5: 'VINE_WHIP', 6: 'TACKLE',
             7: 'RAZOR_LEAF', 8: 'TAKE_DOWN', 9: 'WATER_GUN', 10: 'BITE', 11: 'POUND', 12: 'DOUBLE_SLAP', 13: 'WRAP',
             14: 'HYPER_BEAM', 15: 'LICK', 16: 'DARK_PULSE', 17: 'SMOG', 18: 'SLUDGE', 19: 'METAL_CLAW', 20: 'VICE_GRIP',
             21: 'FLAME_WHEEL', 22: 'MEGAHORN', 23: 'WING_ATTACK', 24: 'FLAMETHROWER', 25: 'SUCKER_PUNCH', 26: 'DIG', 27: 'LOW_KICK',
             28: 'CROSS_CHOP', 29: 'PSYCHO_CUT', 30: 'PSYBEAM', 31: 'EARTHQUAKE', 32: 'STONE_EDGE', 33: 'ICE_PUNCH',
             34: 'HEART_STAMP', 35: 'DISCHARGE', 36: 'FLASH_CANNON', 37: 'PECK', 38: 'DRILL_PECK', 39: 'ICE_BEAM', 40: 'BLIZZARD',
             41: 'AIR_SLASH', 42: 'HEAT_WAVE', 43: 'TWINEEDLE', 44: 'POISON_JAB', 45: 'AERIAL_ACE', 46: 'DRILL_RUN',
             47: 'PETAL_BLIZZARD', 48: 'MEGA_DRAIN', 49: 'BUG_BUZZ', 50: 'POISON_FANG', 51: 'NIGHT_SLASH', 52: 'SLASH',
             53: 'BUBBLE_BEAM', 54: 'SUBMISSION', 55: 'KARATE_CHOP', 56: 'LOW_SWEEP', 57: 'AQUA_JET', 58: 'AQUA_TAIL',
             59: 'SEED_BOMB', 60: 'PSYSHOCK', 61: 'ROCK_THROW', 62: 'ANCIENT_POWER', 63: 'ROCK_TOMB', 64: 'ROCK_SLIDE',
             65: 'POWER_GEM', 66: 'SHADOW_SNEAK', 67: 'SHADOW_PUNCH', 68: 'SHADOW_CLAW', 69: 'OMINOUS_WIND', 70: 'SHADOW_BALL',
             71: 'BULLET_PUNCH', 72: 'MAGNET_BOMB', 73: 'STEEL_WING', 74: 'IRON_HEAD', 75: 'PARABOLIC_CHARGE', 76: 'SPARK',
             77: 'THUNDER_PUNCH', 78: 'THUNDER', 79: 'THUNDERBOLT', 80: 'TWISTER', 81: 'DRAGON_BREATH', 82: 'DRAGON_PULSE',
             83: 'DRAGON_CLAW', 84: 'DISARMING_VOICE', 85: 'DRAINING_KISS', 86: 'DAZZLING_GLEAM', 87: 'MOONBLAST', 88: 'PLAY_ROUGH',
             89: 'CROSS_POISON', 90: 'SLUDGE_BOMB', 91: 'SLUDGE_WAVE', 92: 'GUNK_SHOT', 93: 'MUD_SHOT', 94: 'BONE_CLUB',
             95: 'BULLDOZE', 96: 'MUD_BOMB', 97: 'FURY_CUTTER', 98: 'BUG_BITE', 99: 'SIGNAL_BEAM', 100: 'X_SCISSOR',
             101: 'FLAME_CHARGE', 102: 'FLAME_BURST', 103: 'FIRE_BLAST', 104: 'BRINE', 105: 'WATER_PULSE', 106: 'SCALD',
             107: 'HYDRO_PUMP', 108: 'PSYCHIC', 109: 'PSYSTRIKE', 110: 'ICE_SHARD', 111: 'ICY_WIND', 112: 'FROST_BREATH',
             113: 'ABSORB', 114: 'GIGA_DRAIN', 115: 'FIRE_PUNCH', 116: 'SOLAR_BEAM', 117: 'LEAF_BLADE', 118: 'POWER_WHIP',
             119: 'SPLASH', 120: 'ACID', 121: 'AIR_CUTTER', 122: 'HURRICANE', 123: 'BRICK_BREAK', 124: 'CUT', 125: 'SWIFT',
             126: 'HORN_ATTACK', 127: 'STOMP', 128: 'HEADBUTT', 129: 'HYPER_FANG', 130: 'SLAM', 131: 'BODY_SLAM', 132: 'REST',
             133: 'STRUGGLE', 134: 'SCALD_BLASTOISE', 135: 'HYDRO_PUMP_BLASTOISE', 136: 'WRAP_GREEN', 137: 'WRAP_PINK',
             200: 'FURY_CUTTER_FAST', 201: 'BUG_BITE_FAST', 202: 'BITE_FAST', 203: 'SUCKER_PUNCH_FAST', 204: 'DRAGON_BREATH_FAST',
             205: 'THUNDER_SHOCK_FAST', 206: 'SPARK_FAST', 207: 'LOW_KICK_FAST', 208: 'KARATE_CHOP_FAST', 209: 'EMBER_FAST',
             210: 'WING_ATTACK_FAST', 211: 'PECK_FAST', 212: 'LICK_FAST', 213: 'SHADOW_CLAW_FAST', 214: 'VINE_WHIP_FAST',
             215: 'RAZOR_LEAF_FAST', 216: 'MUD_SHOT_FAST', 217: 'ICE_SHARD_FAST', 218: 'FROST_BREATH_FAST',
             219: 'QUICK_ATTACK_FAST', 220: 'SCRATCH_FAST', 221: 'TACKLE_FAST', 222: 'POUND_FAST', 223: 'CUT_FAST',
             224: 'POISON_JAB_FAST', 225: 'ACID_FAST', 226: 'PSYCHO_CUT_FAST', 227: 'ROCK_THROW_FAST', 228: 'METAL_CLAW_FAST',
             229: 'BULLET_PUNCH_FAST', 230: 'WATER_GUN_FAST', 231: 'SPLASH_FAST', 232: 'WATER_GUN_FAST_BLASTOISE', 233: 'MUD_SLAP_FAST',
             234: 'ZEN_HEADBUTT_FAST', 235: 'CONFUSION_FAST', 236: 'POISON_STING_FAST', 237: 'BUBBLE_FAST', 238: 'FEINT_ATTACK_FAST',
             239: 'STEEL_WING_FAST', 240: 'FIRE_FANG_FAST', 241: 'ROCK_SMASH_FAST'}

pokedex = Pokedex()
