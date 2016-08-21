from __future__ import unicode_literals

from util import ConstReflect


class Rarity(ConstReflect):
    """Enums for pokemon rarity. sort of subjective."""
    CRITTER = 0
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    VERY_RARE = 4
    EPIC = 5
    LEGENDARY = 6
    MYTHIC = 7


class Pokedex(ConstReflect):
    """Class to contain static Pokemon data"""

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

    _evolves = {
        MISSINGNO: 0, BULBASAUR: 25, IVYSAUR: 100, VENUSAUR: 0,
        CHARMANDER: 25, CHARMELEON: 100, CHARIZARD: 0, SQUIRTLE: 25,
        WARTORTLE: 100, BLASTOISE: 0, CATERPIE: 12, METAPOD: 50,
        BUTTERFREE: 0, WEEDLE: 12, KAKUNA: 50, BEEDRILL: 0, PIDGEY: 12,
        PIDGEOTTO: 50, PIDGEOT: 0, RATTATA: 25, RATICATE: 0, SPEAROW: 50,
        FEAROW: 0, EKANS: 50, ARBOK: 0, PIKACHU: 50, RAICHU: 0,
        SANDSHREW: 50, SANDSLASH: 0, NIDORAN_FEMALE: 25, NIDORINA: 100,
        NIDOQUEEN: 0, NIDORAN_MALE: 25, NIDORINO: 100, NIDOKING: 0,
        CLEFAIRY: 50, CLEFABLE: 0, VULPIX: 50, NINETALES: 0, JIGGLYPUFF: 50,
        WIGGLYTUFF: 0, ZUBAT: 50, GOLBAT: 0, ODDISH: 25, GLOOM: 100,
        VILEPLUME: 0, PARAS: 50, PARASECT: 0, VENONAT: 50, VENOMOTH: 0,
        DIGLETT: 50, DUGTRIO: 0, MEOWTH: 50, PERSIAN: 0, PSYDUCK: 50,
        GOLDUCK: 0, MANKEY: 50, PRIMEAPE: 0, GROWLITHE: 50, ARCANINE: 0,
        POLIWAG: 25, POLIWHIRL: 100, POLIWRATH: 0, ABRA: 25, KADABRA: 100,
        ALAKAZAM: 0, MACHOP: 25, MACHOKE: 100, MACHAMP: 0, BELLSPROUT: 25,
        WEEPINBELL: 100, VICTREEBEL: 0, TENTACOOL: 50, TENTACRUEL: 0,
        GEODUDE: 25, GRAVELER: 100, GOLEM: 0, PONYTA: 50, RAPIDASH: 0,
        SLOWPOKE: 50, SLOWBRO: 0, MAGNEMITE: 50, MAGNETON: 0, FARFETCHD: 0,
        DODUO: 50, DODRIO: 0, SEEL: 50, DEWGONG: 0, GRIMER: 50, MUK: 0,
        SHELLDER: 50, CLOYSTER: 0, GASTLY: 25, HAUNTER: 100, GENGAR: 0,
        ONIX: 0, DROWZEE: 50, HYPNO: 0, KRABBY: 50, KINGLER: 0, VOLTORB: 50,
        ELECTRODE: 0, EXEGGCUTE: 50, EXEGGUTOR: 0, CUBONE: 50, MAROWAK: 0,
        HITMONLEE: 0, HITMONCHAN: 0, LICKITUNG: 0, KOFFING: 50, WEEZING: 0,
        RHYHORN: 50, RHYDON: 0, CHANSEY: 0, TANGELA: 0, KANGASKHAN: 0,
        HORSEA: 50, SEADRA: 0, GOLDEEN: 50, SEAKING: 0, STARYU: 50, STARMIE: 0,
        MR_MIME: 0, SCYTHER: 0, JYNX: 0, ELECTABUZZ: 0, MAGMAR: 0, PINSIR: 0,
        TAUROS: 0, MAGIKARP: 400, GYARADOS: 0, LAPRAS: 0, DITTO: 0, EEVEE: 25,
        VAPOREON: 0, JOLTEON: 0, FLAREON: 0, PORYGON: 0, OMANYTE: 50,
        OMASTAR: 0, KABUTO: 50, KABUTOPS: 0, AERODACTYL: 0, SNORLAX: 0,
        ARTICUNO: 0, ZAPDOS: 0, MOLTRES: 0, DRATINI: 25, DRAGONAIR: 100,
        DRAGONITE: 0, MEWTWO: 0, MEW: 0
    }

    _families = {
        BULBASAUR: BULBASAUR, IVYSAUR: BULBASAUR, VENUSAUR: BULBASAUR,
        CHARMANDER: CHARMANDER, CHARMELEON: CHARMANDER, CHARIZARD: CHARMANDER,
        SQUIRTLE: SQUIRTLE, WARTORTLE: SQUIRTLE, BLASTOISE: SQUIRTLE,
        CATERPIE: CATERPIE, METAPOD: CATERPIE, BUTTERFREE: CATERPIE,
        WEEDLE: WEEDLE, KAKUNA: WEEDLE, BEEDRILL: WEEDLE, PIDGEY: PIDGEY,
        PIDGEOTTO: PIDGEY, PIDGEOT: PIDGEY, RATTATA: RATTATA,
        RATICATE: RATTATA, SPEAROW: SPEAROW, FEAROW: SPEAROW, EKANS: EKANS,
        ARBOK: EKANS, PIKACHU: PIKACHU, RAICHU: PIKACHU, SANDSHREW: SANDSHREW,
        SANDSLASH: SANDSHREW, NIDORAN_FEMALE: NIDORAN_FEMALE,
        NIDORINA: NIDORAN_FEMALE, NIDOQUEEN: NIDORAN_FEMALE,
        NIDORAN_MALE: NIDORAN_MALE, NIDORINO: NIDORAN_MALE,
        NIDOKING: NIDORAN_MALE, CLEFAIRY: CLEFAIRY, CLEFABLE: CLEFAIRY,
        VULPIX: VULPIX, NINETALES: VULPIX, JIGGLYPUFF: JIGGLYPUFF,
        WIGGLYTUFF: JIGGLYPUFF, ZUBAT: ZUBAT, GOLBAT: ZUBAT, ODDISH: ODDISH,
        GLOOM: ODDISH, VILEPLUME: ODDISH, PARAS: PARAS, PARASECT: PARAS,
        VENONAT: VENONAT, VENOMOTH: VENONAT, DIGLETT: DIGLETT,
        DUGTRIO: DIGLETT, MEOWTH: MEOWTH, PERSIAN: MEOWTH, PSYDUCK: PSYDUCK,
        GOLDUCK: PSYDUCK, MANKEY: MANKEY, PRIMEAPE: MANKEY,
        GROWLITHE: GROWLITHE, ARCANINE: GROWLITHE, POLIWAG: POLIWAG,
        POLIWHIRL: POLIWAG, POLIWRATH: POLIWAG, ABRA: ABRA, KADABRA: ABRA,
        ALAKAZAM: ABRA, MACHOP: MACHOP, MACHOKE: MACHOP, MACHAMP: MACHOP,
        BELLSPROUT: BELLSPROUT, WEEPINBELL: BELLSPROUT, VICTREEBEL: BELLSPROUT,
        TENTACOOL: TENTACOOL, TENTACRUEL: TENTACOOL, GEODUDE: GEODUDE,
        GRAVELER: GEODUDE, GOLEM: GEODUDE, PONYTA: PONYTA, RAPIDASH: PONYTA,
        SLOWPOKE: SLOWPOKE, SLOWBRO: SLOWPOKE, MAGNEMITE: MAGNEMITE,
        MAGNETON: MAGNEMITE, FARFETCHD: FARFETCHD, DODUO: DODUO, DODRIO: DODUO,
        SEEL: SEEL, DEWGONG: SEEL, GRIMER: GRIMER, MUK: GRIMER,
        SHELLDER: SHELLDER, CLOYSTER: SHELLDER, GASTLY: GASTLY,
        HAUNTER: GASTLY, GENGAR: GASTLY, ONIX: ONIX, DROWZEE: DROWZEE,
        HYPNO: DROWZEE, KRABBY: KRABBY, KINGLER: KRABBY, VOLTORB: VOLTORB,
        ELECTRODE: VOLTORB, EXEGGCUTE: EXEGGCUTE, EXEGGUTOR: EXEGGCUTE,
        CUBONE: CUBONE, MAROWAK: CUBONE, HITMONLEE: HITMONLEE,
        HITMONCHAN: HITMONCHAN, LICKITUNG: LICKITUNG, KOFFING: KOFFING,
        WEEZING: KOFFING, RHYHORN: RHYHORN, RHYDON: RHYHORN, CHANSEY: CHANSEY,
        TANGELA: TANGELA, KANGASKHAN: KANGASKHAN, HORSEA: HORSEA,
        SEADRA: HORSEA, GOLDEEN: GOLDEEN, SEAKING: GOLDEEN, STARYU: STARYU,
        STARMIE: STARYU, MR_MIME: MR_MIME, SCYTHER: SCYTHER, JYNX: JYNX,
        ELECTABUZZ: ELECTABUZZ, MAGMAR: MAGMAR, PINSIR: PINSIR, TAUROS: TAUROS,
        MAGIKARP: MAGIKARP, GYARADOS: MAGIKARP, LAPRAS: LAPRAS, DITTO: DITTO,
        EEVEE: EEVEE, VAPOREON: EEVEE, JOLTEON: JOLTEON, FLAREON: FLAREON,
        PORYGON: PORYGON, OMANYTE: OMANYTE, OMASTAR: OMANYTE, KABUTO: KABUTO,
        KABUTOPS: KABUTO, AERODACTYL: AERODACTYL, SNORLAX: SNORLAX,
        ARTICUNO: ARTICUNO, ZAPDOS: ZAPDOS, MOLTRES: MOLTRES, DRATINI: DRATINI,
        DRAGONAIR: DRATINI, DRAGONITE: DRATINI, MEWTWO: MEWTWO, MEW: MEW
    }

    _rarity = {
        Rarity.MYTHIC: [MEW],
        Rarity.LEGENDARY: [
            ZAPDOS, MOLTRES, MEWTWO, ARTICUNO
        ],
        Rarity.EPIC: [
            DITTO, VENUSAUR, TAUROS, DRAGONITE, CLEFABLE,
            CHARIZARD, BLASTOISE
        ],
        Rarity.VERY_RARE: [
            WEEPINBELL, WARTORTLE, VILEPLUME, VICTREEBEL,
            VENOMOTH, VAPOREON, SLOWBRO, RAICHU, POLIWRATH,
            PINSIR, PIDGEOT, OMASTAR, NIDOQUEEN, NIDOKING,
            MUK, MAROWAK, LAPRAS, KANGASKHAN, KABUTOPS, IVYSAUR,
            GYARADOS, GOLEM, GENGAR, EXEGGUTOR, DRAGONAIR, DEWGONG,
            CHARMELEON, BEEDRILL, ALAKAZAM
        ],
        Rarity.RARE: [
            WIGGLYTUFF, WEEZING, TENTACRUEL, TANGELA,
            STARMIE, SNORLAX, SCYTHER, SEAKING, SEADRA,
            RHYDON, RAPIDASH, PRIMEAPE, PORYGON, POLIWHIRL,
            PARASECT, ONIX, OMANYTE, NINETALES, NIDORINO,
            NIDORINA, MR_MIME, MAGMAR, MACHOKE, MACHAMP,
            LICKITUNG, KINGLER, JOLTEON, HYPNO, HITMONCHAN,
            GLOOM, GOLDUCK, FLAREON, FEAROW, FARFETCHD,
            ELECTABUZZ, DUGTRIO, DRATINI, DODRIO, CLOYSTER,
            CHANSEY, BUTTERFREE, ARCANINE, AERODACTYL
        ],
        Rarity.UNCOMMON: [
            VULPIX, TENTACOOL, STARYU, SQUIRTLE, SPEAROW,
            SHELLDER, SEEL, SANDSLASH, RHYHORN, RATICATE,
            PSYDUCK, PONYTA, PIKACHU, PIDGEOTTO, PERSIAN,
            METAPOD, MAGNETON, KOFFING, KADABRA, KABUTO,
            KAKUNA, JYNX, JIGGLYPUFF, HORSEA, HITMONLEE,
            HAUNTER, GROWLITHE, GRIMER, GRAVELER, GOLBAT,
            EXEGGCUTE, ELECTRODE, CUBONE, CLEFAIRY, CHARMANDER,
            BULBASAUR, ARBOK, ABRA
        ],
        Rarity.COMMON: [
            WEEDLE, VOLTORB, VENONAT, SLOWPOKE, SANDSHREW,
            POLIWAG, PARAS, ODDISH, NIDORAN_MALE, NIDORAN_FEMALE,
            MEOWTH, MANKEY, MAGNEMITE, MAGIKARP, MACHOP, KRABBY,
            GOLDEEN, GEODUDE, GASTLY, EEVEE, EKANS, DROWZEE,
            DODUO, DIGLETT, CATERPIE, BELLSPROUT
        ],
        Rarity.CRITTER: [ZUBAT, PIDGEY, RATTATA]
    }

    def getRarityById(self, pokemonId):
        for rarity in self.rarity:
            if pokemonId in self._rarity[rarity]:
                return rarity
        return 0

    def getRarityByName(self, name):
        return self.getRarityById(self[name])

    @property
    def rarity(self):
        return self._rarity

    @property
    def families(self):
        return self._families

    @property
    def evolves(self):
        return self._evolves

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

move_details = [{
    "ID": 13,
    "Name": "Wrap",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Normal",
    "Power": 15,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.06,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 4000,
    "Damage Window Start (ms)": 2800,
    "Damage Window End (ms)": 3400,
    "Energy Delta": -20
}, {
    "ID": 14,
    "Name": "Hyper Beam",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Normal",
    "Power": 70,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.15,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 5000,
    "Damage Window Start (ms)": 4000,
    "Damage Window End (ms)": 4800,
    "Energy Delta": -100
}, {
    "ID": 16,
    "Name": "Dark Pulse",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Dark",
    "Power": 45,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.08,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3500,
    "Damage Window Start (ms)": 2300,
    "Damage Window End (ms)": 3400,
    "Energy Delta": -33
}, {
    "ID": 18,
    "Name": "Sludge",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Poison",
    "Power": 25,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.065,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2600,
    "Damage Window Start (ms)": 1850,
    "Damage Window End (ms)": 2350,
    "Energy Delta": -25
}, {
    "ID": 20,
    "Name": "Vice Grip",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Normal",
    "Power": 15,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.055,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2100,
    "Damage Window Start (ms)": 1850,
    "Damage Window End (ms)": 2100,
    "Energy Delta": -20
}, {
    "ID": 21,
    "Name": "Flame Wheel",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Fire",
    "Power": 35,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.06,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 4600,
    "Damage Window Start (ms)": 2700,
    "Damage Window End (ms)": 3200,
    "Energy Delta": -25
}, {
    "ID": 22,
    "Name": "Megahorn",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Bug",
    "Power": 55,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.12,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3200,
    "Damage Window Start (ms)": 2400,
    "Damage Window End (ms)": 2700,
    "Energy Delta": -100
}, {
    "ID": 24,
    "Name": "Flamethrower",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Fire",
    "Power": 50,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.09,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2900,
    "Damage Window Start (ms)": 1700,
    "Damage Window End (ms)": 2600,
    "Energy Delta": -50
}, {
    "ID": 26,
    "Name": "Dig",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Ground",
    "Power": 45,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.08,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 5800,
    "Damage Window Start (ms)": 4600,
    "Damage Window End (ms)": 5000,
    "Energy Delta": -33
}, {
    "ID": 28,
    "Name": "Cross Chop",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Fighting",
    "Power": 55,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.1,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2000,
    "Damage Window Start (ms)": 1500,
    "Damage Window End (ms)": 1800,
    "Energy Delta": -100
}, {
    "ID": 30,
    "Name": "Psybeam",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Psychic",
    "Power": 35,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.065,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3800,
    "Damage Window Start (ms)": 2300,
    "Damage Window End (ms)": 3600,
    "Energy Delta": -25
}, {
    "ID": 31,
    "Name": "Earthquake",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Ground",
    "Power": 60,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.1,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 4200,
    "Damage Window Start (ms)": 2000,
    "Damage Window End (ms)": 3950,
    "Energy Delta": -100
}, {
    "ID": 32,
    "Name": "Stone Edge",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Rock",
    "Power": 55,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.1,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3100,
    "Damage Window Start (ms)": 1400,
    "Damage Window End (ms)": 1800,
    "Energy Delta": -100
}, {
    "ID": 33,
    "Name": "Ice Punch",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Ice",
    "Power": 45,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.075,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3500,
    "Damage Window Start (ms)": 2100,
    "Damage Window End (ms)": 3200,
    "Energy Delta": -33
}, {
    "ID": 34,
    "Name": "Heart Stamp",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Psychic",
    "Power": 20,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.06,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2550,
    "Damage Window Start (ms)": 1950,
    "Damage Window End (ms)": 2250,
    "Energy Delta": -25
}, {
    "ID": 35,
    "Name": "Discharge",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Electric",
    "Power": 40,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.08,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2500,
    "Damage Window Start (ms)": 1600,
    "Damage Window End (ms)": 2300,
    "Energy Delta": -33
}, {
    "ID": 36,
    "Name": "Flash Cannon",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Steel",
    "Power": 55,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.08,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3900,
    "Damage Window Start (ms)": 2400,
    "Damage Window End (ms)": 3500,
    "Energy Delta": -33
}, {
    "ID": 38,
    "Name": "Drill Peck",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Flying",
    "Power": 30,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.08,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2700,
    "Damage Window Start (ms)": 1600,
    "Damage Window End (ms)": 2500,
    "Energy Delta": -33
}, {
    "ID": 39,
    "Name": "Ice Beam",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Ice",
    "Power": 50,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.09,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3650,
    "Damage Window Start (ms)": 2150,
    "Damage Window End (ms)": 3500,
    "Energy Delta": -50
}, {
    "ID": 40,
    "Name": "Blizzard",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Ice",
    "Power": 60,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.11,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3900,
    "Damage Window Start (ms)": 3600,
    "Damage Window End (ms)": 3600,
    "Energy Delta": -100
}, {
    "ID": 42,
    "Name": "Heat Wave",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Fire",
    "Power": 60,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.095,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3800,
    "Damage Window Start (ms)": 3000,
    "Damage Window End (ms)": 3400,
    "Energy Delta": -100
}, {
    "ID": 45,
    "Name": "Aerial Ace",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Flying",
    "Power": 25,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.06,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2900,
    "Damage Window Start (ms)": 2000,
    "Damage Window End (ms)": 2600,
    "Energy Delta": -25
}, {
    "ID": 46,
    "Name": "Drill Run",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Ground",
    "Power": 40,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.08,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3400,
    "Damage Window Start (ms)": 2100,
    "Damage Window End (ms)": 2800,
    "Energy Delta": -33
}, {
    "ID": 47,
    "Name": "Petal Blizzard",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Grass",
    "Power": 50,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.09,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3200,
    "Damage Window Start (ms)": 2100,
    "Damage Window End (ms)": 3100,
    "Energy Delta": -50
}, {
    "ID": 48,
    "Name": "Mega Drain",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Grass",
    "Power": 15,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.04,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3200,
    "Damage Window Start (ms)": 1400,
    "Damage Window End (ms)": 2600,
    "Energy Delta": -20
}, {
    "ID": 49,
    "Name": "Bug Buzz",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Bug",
    "Power": 50,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.09,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 4250,
    "Damage Window Start (ms)": 2600,
    "Damage Window End (ms)": 4100,
    "Energy Delta": -50
}, {
    "ID": 50,
    "Name": "Poison Fang",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Poison",
    "Power": 15,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.05,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2400,
    "Damage Window Start (ms)": 1650,
    "Damage Window End (ms)": 1850,
    "Energy Delta": -20
}, {
    "ID": 51,
    "Name": "Night Slash",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Dark",
    "Power": 25,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.07,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2700,
    "Damage Window Start (ms)": 2400,
    "Damage Window End (ms)": 2600,
    "Energy Delta": -25
}, {
    "ID": 53,
    "Name": "Bubble Beam",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Water",
    "Power": 25,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.065,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2900,
    "Damage Window Start (ms)": 2600,
    "Damage Window End (ms)": 2800,
    "Energy Delta": -25
}, {
    "ID": 54,
    "Name": "Submission",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Fighting",
    "Power": 30,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.08,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2100,
    "Damage Window Start (ms)": 1850,
    "Damage Window End (ms)": 2000,
    "Energy Delta": -33
}, {
    "ID": 56,
    "Name": "Low Sweep",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Fighting",
    "Power": 25,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.065,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2250,
    "Damage Window Start (ms)": 2000,
    "Damage Window End (ms)": 2150,
    "Energy Delta": -25
}, {
    "ID": 57,
    "Name": "Aqua Jet",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Water",
    "Power": 15,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.04,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2350,
    "Damage Window Start (ms)": 1700,
    "Damage Window End (ms)": 2100,
    "Energy Delta": -20
}, {
    "ID": 58,
    "Name": "Aqua Tail",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Water",
    "Power": 50,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.09,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2350,
    "Damage Window Start (ms)": 2050,
    "Damage Window End (ms)": 2250,
    "Energy Delta": -50
}, {
    "ID": 59,
    "Name": "Seed Bomb",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Grass",
    "Power": 30,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.08,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2400,
    "Damage Window Start (ms)": 1300,
    "Damage Window End (ms)": 1800,
    "Energy Delta": -33
}, {
    "ID": 60,
    "Name": "Psyshock",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Psychic",
    "Power": 40,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.08,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2700,
    "Damage Window Start (ms)": 2200,
    "Damage Window End (ms)": 2700,
    "Energy Delta": -33
}, {
    "ID": 62,
    "Name": "Ancient Power",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Rock",
    "Power": 30,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.06,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3600,
    "Damage Window Start (ms)": 2900,
    "Damage Window End (ms)": 3250,
    "Energy Delta": -25
}, {
    "ID": 63,
    "Name": "Rock Tomb",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Rock",
    "Power": 25,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.06,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3400,
    "Damage Window Start (ms)": 2300,
    "Damage Window End (ms)": 3200,
    "Energy Delta": -25
}, {
    "ID": 64,
    "Name": "Rock Slide",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Rock",
    "Power": 40,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.075,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3200,
    "Damage Window Start (ms)": 1500,
    "Damage Window End (ms)": 2900,
    "Energy Delta": -33
}, {
    "ID": 65,
    "Name": "Power Gem",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Rock",
    "Power": 40,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.08,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2900,
    "Damage Window Start (ms)": 2000,
    "Damage Window End (ms)": 2800,
    "Energy Delta": -33
}, {
    "ID": 66,
    "Name": "Shadow Sneak",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Ghost",
    "Power": 15,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.04,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3100,
    "Damage Window Start (ms)": 2300,
    "Damage Window End (ms)": 2900,
    "Energy Delta": -20
}, {
    "ID": 67,
    "Name": "Shadow Punch",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Ghost",
    "Power": 20,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.06,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2100,
    "Damage Window Start (ms)": 1400,
    "Damage Window End (ms)": 1700,
    "Energy Delta": -25
}, {
    "ID": 69,
    "Name": "Ominous Wind",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Ghost",
    "Power": 25,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.06,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3100,
    "Damage Window Start (ms)": 1850,
    "Damage Window End (ms)": 2100,
    "Energy Delta": -25
}, {
    "ID": 70,
    "Name": "Shadow Ball",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Ghost",
    "Power": 40,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.08,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3080,
    "Damage Window Start (ms)": 2300,
    "Damage Window End (ms)": 2600,
    "Energy Delta": -33
}, {
    "ID": 72,
    "Name": "Magnet Bomb",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Steel",
    "Power": 25,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.06,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2800,
    "Damage Window Start (ms)": 1750,
    "Damage Window End (ms)": 2300,
    "Energy Delta": -25
}, {
    "ID": 74,
    "Name": "Iron Head",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Steel",
    "Power": 40,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.08,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2000,
    "Damage Window Start (ms)": 1550,
    "Damage Window End (ms)": 1800,
    "Energy Delta": -33
}, {
    "ID": 75,
    "Name": "Parabolic Charge",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Electric",
    "Power": 15,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.05,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2100,
    "Damage Window Start (ms)": 1300,
    "Damage Window End (ms)": 1700,
    "Energy Delta": -20
}, {
    "ID": 77,
    "Name": "Thunder Punch",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Electric",
    "Power": 40,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.075,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2400,
    "Damage Window Start (ms)": 1950,
    "Damage Window End (ms)": 2200,
    "Energy Delta": -33
}, {
    "ID": 78,
    "Name": "Thunder",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Electric",
    "Power": 65,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.11,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 4300,
    "Damage Window Start (ms)": 2550,
    "Damage Window End (ms)": 4100,
    "Energy Delta": -100
}, {
    "ID": 79,
    "Name": "Thunderbolt",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Electric",
    "Power": 50,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.09,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2700,
    "Damage Window Start (ms)": 1900,
    "Damage Window End (ms)": 2700,
    "Energy Delta": -50
}, {
    "ID": 80,
    "Name": "Twister",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Dragon",
    "Power": 15,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.04,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2700,
    "Damage Window Start (ms)": 850,
    "Damage Window End (ms)": 2600,
    "Energy Delta": -20
}, {
    "ID": 82,
    "Name": "Dragon Pulse",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Dragon",
    "Power": 50,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.085,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3600,
    "Damage Window Start (ms)": 2100,
    "Damage Window End (ms)": 3300,
    "Energy Delta": -50
}, {
    "ID": 83,
    "Name": "Dragon Claw",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Dragon",
    "Power": 40,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.08,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 1500,
    "Damage Window Start (ms)": 1200,
    "Damage Window End (ms)": 1400,
    "Energy Delta": -50
}, {
    "ID": 84,
    "Name": "Disarming Voice",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Fairy",
    "Power": 20,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.04,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3900,
    "Damage Window Start (ms)": 1800,
    "Damage Window End (ms)": 3600,
    "Energy Delta": -20
}, {
    "ID": 85,
    "Name": "Draining Kiss",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Fairy",
    "Power": 15,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.05,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2800,
    "Damage Window Start (ms)": 1000,
    "Damage Window End (ms)": 1100,
    "Energy Delta": -20
}, {
    "ID": 86,
    "Name": "Dazzling Gleam",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Fairy",
    "Power": 45,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.08,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 4200,
    "Damage Window Start (ms)": 3300,
    "Damage Window End (ms)": 4100,
    "Energy Delta": -33
}, {
    "ID": 87,
    "Name": "Moonblast",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Fairy",
    "Power": 60,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.095,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 4100,
    "Damage Window Start (ms)": 3500,
    "Damage Window End (ms)": 4100,
    "Energy Delta": -100
}, {
    "ID": 88,
    "Name": "Play Rough",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Fairy",
    "Power": 50,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.1,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2900,
    "Damage Window Start (ms)": 1400,
    "Damage Window End (ms)": 2700,
    "Energy Delta": -50
}, {
    "ID": 89,
    "Name": "Cross Poison",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Poison",
    "Power": 20,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.07,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 1500,
    "Damage Window Start (ms)": 1200,
    "Damage Window End (ms)": 1500,
    "Energy Delta": -25
}, {
    "ID": 90,
    "Name": "Sludge Bomb",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Poison",
    "Power": 50,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.09,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2600,
    "Damage Window Start (ms)": 1950,
    "Damage Window End (ms)": 2450,
    "Energy Delta": -50
}, {
    "ID": 91,
    "Name": "Sludge Wave",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Poison",
    "Power": 60,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.095,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3400,
    "Damage Window Start (ms)": 2400,
    "Damage Window End (ms)": 3300,
    "Energy Delta": -100
}, {
    "ID": 92,
    "Name": "Gunk Shot",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Poison",
    "Power": 60,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.12,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3000,
    "Damage Window Start (ms)": 2000,
    "Damage Window End (ms)": 2400,
    "Energy Delta": -100
}, {
    "ID": 94,
    "Name": "Bone Club",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Ground",
    "Power": 20,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.065,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 1600,
    "Damage Window Start (ms)": 1250,
    "Damage Window End (ms)": 1500,
    "Energy Delta": -25
}, {
    "ID": 95,
    "Name": "Bulldoze",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Ground",
    "Power": 30,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.06,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3400,
    "Damage Window Start (ms)": 1900,
    "Damage Window End (ms)": 3000,
    "Energy Delta": -25
}, {
    "ID": 96,
    "Name": "Mud Bomb",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Ground",
    "Power": 25,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.065,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2600,
    "Damage Window Start (ms)": 2050,
    "Damage Window End (ms)": 2500,
    "Energy Delta": -25
}, {
    "ID": 99,
    "Name": "Signal Beam",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Bug",
    "Power": 35,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.075,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3100,
    "Damage Window Start (ms)": 2000,
    "Damage Window End (ms)": 3000,
    "Energy Delta": -33
}, {
    "ID": 100,
    "Name": "X Scissor",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Bug",
    "Power": 30,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.08,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2100,
    "Damage Window Start (ms)": 1350,
    "Damage Window End (ms)": 1600,
    "Energy Delta": -33
}, {
    "ID": 101,
    "Name": "Flame Charge",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Fire",
    "Power": 20,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.05,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3100,
    "Damage Window Start (ms)": 2700,
    "Damage Window End (ms)": 2900,
    "Energy Delta": -20
}, {
    "ID": 102,
    "Name": "Flame Burst",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Fire",
    "Power": 25,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.07,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2100,
    "Damage Window Start (ms)": 1200,
    "Damage Window End (ms)": 1600,
    "Energy Delta": -25
}, {
    "ID": 103,
    "Name": "Fire Blast",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Fire",
    "Power": 60,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.11,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 4100,
    "Damage Window Start (ms)": 3600,
    "Damage Window End (ms)": 4000,
    "Energy Delta": -100
}, {
    "ID": 104,
    "Name": "Brine",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Water",
    "Power": 20,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.065,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2400,
    "Damage Window Start (ms)": 1650,
    "Damage Window End (ms)": 2000,
    "Energy Delta": -25
}, {
    "ID": 105,
    "Name": "Water Pulse",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Water",
    "Power": 30,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.06,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3300,
    "Damage Window Start (ms)": 1900,
    "Damage Window End (ms)": 2900,
    "Energy Delta": -25
}, {
    "ID": 106,
    "Name": "Scald",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Water",
    "Power": 35,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.08,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 4000,
    "Damage Window Start (ms)": 1800,
    "Damage Window End (ms)": 3900,
    "Energy Delta": -33
}, {
    "ID": 107,
    "Name": "Hydro Pump",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Water",
    "Power": 60,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.11,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3800,
    "Damage Window Start (ms)": 1500,
    "Damage Window End (ms)": 3600,
    "Energy Delta": -100
}, {
    "ID": 108,
    "Name": "Psychic",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Psychic",
    "Power": 50,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.09,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2800,
    "Damage Window Start (ms)": 1600,
    "Damage Window End (ms)": 2800,
    "Energy Delta": -50
}, {
    "ID": 109,
    "Name": "Psystrike",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Psychic",
    "Power": 70,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.1,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 5100,
    "Damage Window Start (ms)": 4400,
    "Damage Window End (ms)": 5300,
    "Energy Delta": -100
}, {
    "ID": 111,
    "Name": "Icy Wind",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Ice",
    "Power": 15,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.055,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3800,
    "Damage Window Start (ms)": 2000,
    "Damage Window End (ms)": 2700,
    "Energy Delta": -20
}, {
    "ID": 114,
    "Name": "Giga Drain",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Grass",
    "Power": 35,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.075,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3600,
    "Damage Window Start (ms)": 350,
    "Damage Window End (ms)": 1500,
    "Energy Delta": -33
}, {
    "ID": 115,
    "Name": "Fire Punch",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Fire",
    "Power": 35,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.075,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2800,
    "Damage Window Start (ms)": 1690,
    "Damage Window End (ms)": 2200,
    "Energy Delta": -33
}, {
    "ID": 116,
    "Name": "Solar Beam",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Grass",
    "Power": 65,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.12,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 4900,
    "Damage Window Start (ms)": 3100,
    "Damage Window End (ms)": 4800,
    "Energy Delta": -100
}, {
    "ID": 117,
    "Name": "Leaf Blade",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Grass",
    "Power": 45,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.09,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2800,
    "Damage Window Start (ms)": 1200,
    "Damage Window End (ms)": 2200,
    "Energy Delta": -50
}, {
    "ID": 118,
    "Name": "Power Whip",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Grass",
    "Power": 60,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.12,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2800,
    "Damage Window Start (ms)": 1500,
    "Damage Window End (ms)": 2800,
    "Energy Delta": -100
}, {
    "ID": 121,
    "Name": "Air Cutter",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Flying",
    "Power": 25,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.06,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3300,
    "Damage Window Start (ms)": 2200,
    "Damage Window End (ms)": 3100,
    "Energy Delta": -25
}, {
    "ID": 122,
    "Name": "Hurricane",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Flying",
    "Power": 60,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.11,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3200,
    "Damage Window Start (ms)": 1030,
    "Damage Window End (ms)": 2800,
    "Energy Delta": -100
}, {
    "ID": 123,
    "Name": "Brick Break",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Fighting",
    "Power": 30,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.075,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 1600,
    "Damage Window Start (ms)": 1100,
    "Damage Window End (ms)": 1500,
    "Energy Delta": -33
}, {
    "ID": 125,
    "Name": "Swift",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Normal",
    "Power": 25,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.06,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3000,
    "Damage Window Start (ms)": 2300,
    "Damage Window End (ms)": 2800,
    "Energy Delta": -25
}, {
    "ID": 126,
    "Name": "Horn Attack",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Normal",
    "Power": 20,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.065,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2200,
    "Damage Window Start (ms)": 1600,
    "Damage Window End (ms)": 1900,
    "Energy Delta": -25
}, {
    "ID": 127,
    "Name": "Stomp",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Normal",
    "Power": 25,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.065,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2100,
    "Damage Window Start (ms)": 1200,
    "Damage Window End (ms)": 1900,
    "Energy Delta": -25
}, {
    "ID": 129,
    "Name": "Hyper Fang",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Normal",
    "Power": 35,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.08,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2100,
    "Damage Window Start (ms)": 1700,
    "Damage Window End (ms)": 2000,
    "Energy Delta": -33
}, {
    "ID": 131,
    "Name": "Body Slam",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Normal",
    "Power": 50,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.085,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 1560,
    "Damage Window Start (ms)": 1100,
    "Damage Window End (ms)": 1300,
    "Energy Delta": -50
}, {
    "ID": 132,
    "Name": "Rest",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Normal",
    "Power": 35,
    "Accuracy Chance": 1,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3100,
    "Damage Window Start (ms)": 1395,
    "Damage Window End (ms)": 2691,
    "Energy Delta": -33
}, {
    "ID": 133,
    "Name": "Struggle",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Normal",
    "Power": 15,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.1,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 1695,
    "Damage Window Start (ms)": 800,
    "Damage Window End (ms)": 1500,
    "Energy Delta": -20
}, {
    "ID": 134,
    "Name": "Scald Blastoise",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Water",
    "Power": 35,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.08,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 4000,
    "Damage Window Start (ms)": 1800,
    "Damage Window End (ms)": 3900,
    "Energy Delta": -33
}, {
    "ID": 135,
    "Name": "Hydro Pump Blastoise",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Water",
    "Power": 60,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.11,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3800,
    "Damage Window Start (ms)": 1500,
    "Damage Window End (ms)": 3600,
    "Energy Delta": -100
}, {
    "ID": 136,
    "Name": "Wrap Green",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Normal",
    "Power": 15,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.06,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3700,
    "Damage Window Start (ms)": 2200,
    "Damage Window End (ms)": 3200,
    "Energy Delta": -20
}, {
    "ID": 137,
    "Name": "Wrap Pink",
    "Move Type": "Charge",
    "Animation ID": 5,
    "Type": "Normal",
    "Power": 15,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.06,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 3700,
    "Damage Window Start (ms)": 2200,
    "Damage Window End (ms)": 3200,
    "Energy Delta": -20
}, {
    "ID": 200,
    "Name": "Fury Cutter",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Bug",
    "Power": 3,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 400,
    "Damage Window Start (ms)": 200,
    "Damage Window End (ms)": 400,
    "Energy Delta": 12
}, {
    "ID": 201,
    "Name": "Bug Bite",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Bug",
    "Power": 6,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 450,
    "Damage Window Start (ms)": 250,
    "Damage Window End (ms)": 450,
    "Energy Delta": 7
}, {
    "ID": 202,
    "Name": "Bite",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Dark",
    "Power": 6,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 500,
    "Damage Window Start (ms)": 300,
    "Damage Window End (ms)": 500,
    "Energy Delta": 7
}, {
    "ID": 203,
    "Name": "Sucker Punch",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Dark",
    "Power": 7,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 700,
    "Damage Window Start (ms)": 500,
    "Damage Window End (ms)": 700,
    "Energy Delta": 4
}, {
    "ID": 204,
    "Name": "Dragon Breath",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Dragon",
    "Power": 6,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 500,
    "Damage Window Start (ms)": 300,
    "Damage Window End (ms)": 500,
    "Energy Delta": 7
}, {
    "ID": 205,
    "Name": "Thunder Shock",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Electric",
    "Power": 5,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 600,
    "Damage Window Start (ms)": 400,
    "Damage Window End (ms)": 600,
    "Energy Delta": 7
}, {
    "ID": 206,
    "Name": "Spark",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Electric",
    "Power": 7,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 700,
    "Damage Window Start (ms)": 500,
    "Damage Window End (ms)": 700,
    "Energy Delta": 4
}, {
    "ID": 207,
    "Name": "Low Kick",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Fighting",
    "Power": 5,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 600,
    "Damage Window Start (ms)": 400,
    "Damage Window End (ms)": 600,
    "Energy Delta": 7
}, {
    "ID": 208,
    "Name": "Karate Chop",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Fighting",
    "Power": 6,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 800,
    "Damage Window Start (ms)": 600,
    "Damage Window End (ms)": 800,
    "Energy Delta": 7
}, {
    "ID": 209,
    "Name": "Ember",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Fire",
    "Power": 10,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 1050,
    "Damage Window Start (ms)": 850,
    "Damage Window End (ms)": 1050,
    "Energy Delta": 7
}, {
    "ID": 210,
    "Name": "Wing Attack",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Flying",
    "Power": 12,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 750,
    "Damage Window Start (ms)": 550,
    "Damage Window End (ms)": 750,
    "Energy Delta": 7
}, {
    "ID": 211,
    "Name": "Peck",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Flying",
    "Power": 10,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 1150,
    "Damage Window Start (ms)": 950,
    "Damage Window End (ms)": 1150,
    "Energy Delta": 10
}, {
    "ID": 212,
    "Name": "Lick",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Ghost",
    "Power": 10,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 500,
    "Damage Window Start (ms)": 300,
    "Damage Window End (ms)": 500,
    "Energy Delta": 7
}, {
    "ID": 213,
    "Name": "Shadow Claw",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Ghost",
    "Power": 16,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 950,
    "Damage Window Start (ms)": 750,
    "Damage Window End (ms)": 950,
    "Energy Delta": 7
}, {
    "ID": 214,
    "Name": "Vine Whip",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Grass",
    "Power": 10,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 650,
    "Damage Window Start (ms)": 450,
    "Damage Window End (ms)": 650,
    "Energy Delta": 7
}, {
    "ID": 215,
    "Name": "Razor Leaf",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Grass",
    "Power": 15,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 1450,
    "Damage Window Start (ms)": 1250,
    "Damage Window End (ms)": 1450,
    "Energy Delta": 7
}, {
    "ID": 216,
    "Name": "Mud Shot",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Ground",
    "Power": 12,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 550,
    "Damage Window Start (ms)": 350,
    "Damage Window End (ms)": 550,
    "Energy Delta": 7
}, {
    "ID": 217,
    "Name": "Ice Shard",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Ice",
    "Power": 10,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 1400,
    "Damage Window Start (ms)": 1200,
    "Damage Window End (ms)": 1400,
    "Energy Delta": 7
}, {
    "ID": 218,
    "Name": "Frost Breath",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Ice",
    "Power": 12,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 810,
    "Damage Window Start (ms)": 610,
    "Damage Window End (ms)": 810,
    "Energy Delta": 7
}, {
    "ID": 219,
    "Name": "Quick Attack",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Normal",
    "Power": 10,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 1330,
    "Damage Window Start (ms)": 1130,
    "Damage Window End (ms)": 1330,
    "Energy Delta": 7
}, {
    "ID": 220,
    "Name": "Scratch",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Normal",
    "Power": 10,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 500,
    "Damage Window Start (ms)": 300,
    "Damage Window End (ms)": 500,
    "Energy Delta": 7
}, {
    "ID": 221,
    "Name": "Tackle",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Normal",
    "Power": 12,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 1100,
    "Damage Window Start (ms)": 900,
    "Damage Window End (ms)": 1100,
    "Energy Delta": 7
}, {
    "ID": 222,
    "Name": "Pound",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Normal",
    "Power": 8,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 540,
    "Damage Window Start (ms)": 340,
    "Damage Window End (ms)": 540,
    "Energy Delta": 7
}, {
    "ID": 223,
    "Name": "Cut",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Normal",
    "Power": 12,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 1130,
    "Damage Window Start (ms)": 930,
    "Damage Window End (ms)": 1130,
    "Energy Delta": 7
}, {
    "ID": 224,
    "Name": "Poison Jab",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Poison",
    "Power": 15,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 1050,
    "Damage Window Start (ms)": 850,
    "Damage Window End (ms)": 1050,
    "Energy Delta": 7
}, {
    "ID": 225,
    "Name": "Acid",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Poison",
    "Power": 10,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 1050,
    "Damage Window Start (ms)": 850,
    "Damage Window End (ms)": 1050,
    "Energy Delta": 7
}, {
    "ID": 226,
    "Name": "Psycho Cut",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Psychic",
    "Power": 15,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 570,
    "Damage Window Start (ms)": 370,
    "Damage Window End (ms)": 570,
    "Energy Delta": 7
}, {
    "ID": 227,
    "Name": "Rock Throw",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Rock",
    "Power": 12,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 1360,
    "Damage Window Start (ms)": 1160,
    "Damage Window End (ms)": 1360,
    "Energy Delta": 7
}, {
    "ID": 228,
    "Name": "Metal Claw",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Steel",
    "Power": 12,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 630,
    "Damage Window Start (ms)": 430,
    "Damage Window End (ms)": 630,
    "Energy Delta": 7
}, {
    "ID": 229,
    "Name": "Bullet Punch",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Steel",
    "Power": 10,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 1200,
    "Damage Window Start (ms)": 1000,
    "Damage Window End (ms)": 1200,
    "Energy Delta": 7
}, {
    "ID": 230,
    "Name": "Water Gun",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Water",
    "Power": 10,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 500,
    "Damage Window Start (ms)": 300,
    "Damage Window End (ms)": 500,
    "Energy Delta": 7
}, {
    "ID": 231,
    "Name": "Splash",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Water",
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 1230,
    "Damage Window Start (ms)": 1030,
    "Damage Window End (ms)": 1230,
    "Energy Delta": 7,
    "Power": 0
}, {
    "ID": 232,
    "Name": "Water Gun Fast Blastoise",
    "Move Type": "Charge",
    "Animation ID": 4,
    "Type": "Water",
    "Power": 10,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 500,
    "Damage Window Start (ms)": 300,
    "Damage Window End (ms)": 500,
    "Energy Delta": 7
}, {
    "ID": 233,
    "Name": "Mud Slap",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Ground",
    "Power": 6,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 1350,
    "Damage Window Start (ms)": 1150,
    "Damage Window End (ms)": 1350,
    "Energy Delta": 9
}, {
    "ID": 234,
    "Name": "Zen Headbutt",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Psychic",
    "Power": 15,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 1050,
    "Damage Window Start (ms)": 850,
    "Damage Window End (ms)": 1050,
    "Energy Delta": 4
}, {
    "ID": 235,
    "Name": "Confusion",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Psychic",
    "Power": 12,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 1510,
    "Damage Window Start (ms)": 1310,
    "Damage Window End (ms)": 1510,
    "Energy Delta": 7
}, {
    "ID": 236,
    "Name": "Poison Sting",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Poison",
    "Power": 6,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 575,
    "Damage Window Start (ms)": 375,
    "Damage Window End (ms)": 575,
    "Energy Delta": 4
}, {
    "ID": 237,
    "Name": "Bubble",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Water",
    "Power": 15,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 2300,
    "Damage Window Start (ms)": 2100,
    "Damage Window End (ms)": 2300,
    "Energy Delta": 15
}, {
    "ID": 238,
    "Name": "Feint Attack",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Dark",
    "Power": 12,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 1040,
    "Damage Window Start (ms)": 840,
    "Damage Window End (ms)": 1040,
    "Energy Delta": 7
}, {
    "ID": 239,
    "Name": "Steel Wing",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Steel",
    "Power": 15,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 1330,
    "Damage Window Start (ms)": 1130,
    "Damage Window End (ms)": 1330,
    "Energy Delta": 4
}, {
    "ID": 240,
    "Name": "Fire Fang",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Fire",
    "Power": 7,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 840,
    "Damage Window Start (ms)": 640,
    "Damage Window End (ms)": 840,
    "Energy Delta": 4
}, {
    "ID": 241,
    "Name": "Rock Smash",
    "Move Type": "Quick",
    "Animation ID": 4,
    "Type": "Fighting",
    "Power": 5,
    "Accuracy Chance": 1,
    "Stamina Loss Scalar": 0.01,
    "Trainer Level Min": 1,
    "Trainer Level Max": 100,
    "Duration (ms)": 1410,
    "Damage Window Start (ms)": 1210,
    "Damage Window End (ms)": 1410,
    "Energy Delta": 7
}]

pokedex = Pokedex()
