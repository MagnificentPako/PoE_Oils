from enum import Enum
from functools import total_ordering
from colored import fg

@total_ordering
class Oil(Enum):
    CLEAR = 1,
    SEPIA = 2,
    AMBER = 3,
    VERDANT = 4,
    TEAL = 5,
    AZURE = 6,
    INDIGO = 7,
    VIOLET = 8,
    CRIMSON = 9,
    BLACK = 10,
    OPALESCENT = 11,
    SILVER = 12,
    GOLDEN = 13,
    UNKNOWN = 14

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

    def __repr__(self):
        return "%s%s %sOil" % (fg(oil_color[self]), (self.name[0] + self.name[1:].lower()), fg(15))

oil_map = {
    'Clear Oil': Oil.CLEAR,
    'Sepia Oil': Oil.SEPIA,
    'Amber Oil': Oil.AMBER,
    'Verdant Oil': Oil.VERDANT,
    'Teal Oil': Oil.TEAL,
    'Azure Oil': Oil.AZURE,
    'Indigo Oil': Oil.INDIGO,
    'Violet Oil': Oil.VIOLET,
    'Crimson Oil': Oil.CRIMSON,
    'Black Oil': Oil.BLACK,
    'Opalescent Oil': Oil.OPALESCENT,
    'Silver Oil': Oil.SILVER,
    'Golden Oil': Oil.GOLDEN
} 

oil_color = {
    Oil.CLEAR: 7,
    Oil.SEPIA: 94,
    Oil.AMBER: 166,
    Oil.VERDANT: 82,
    Oil.TEAL: 87,
    Oil.AZURE: 21,
    Oil.INDIGO: 129,
    Oil.VIOLET: 200,
    Oil.CRIMSON: 1,
    Oil.BLACK: 238,
    Oil.OPALESCENT: 182,
    Oil.SILVER: 252,
    Oil.GOLDEN: 184
}

class Anoint():
    def __init__(self, oils, effect):
        self.oils = oils
        self.effect = effect

    def __repr__(self):
        return str(self.oils) + ": " + self.effect