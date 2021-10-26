import random


class Spell:
    def __init__(self, name, dmg, cost, type):
        self.name = name
        self.dmg = dmg
        self.cost = cost
        self.type = type

    def get_spell_dmg(self):
        dmg = random.randrange(self.dmg-10, self.dmg+10)
        return dmg
