import random
from classes.magic import Spell


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLIE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atck, defense, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atckl = atck - 10
        self.atckh = atck + 10
        self.defense = defense
        self.magic = magic
        self.items = items
        self.actions = ['Attack', 'Magic', 'Items']
        self.name = name

    def generate_damage(self):
        return random.randrange(self.atckl, self.atckh)

    def generate_spell_damage(self, i):
        return self.magic[i].get_spell_dmg()

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

    def get_healed(self, dmg):
        self.hp = min(self.maxhp, self.hp + dmg)

    def choose_action(self):
        print(self.name + ": ")
        print(Colors.OKBLUE + Colors.BOLD + "Action" + Colors.ENDC)
        i = 1
        for action in self.actions:
            print(str(i) + ": " + action)
            i += 1

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_spell_name(self, i):
        return self.magic[i].name

    def get_spell_cost(self, i):
        return self.magic[i].cost

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_spell(self, i):
        return self.magic[i]

    def choose_magic(self):
        print(Colors.OKBLUE + "MAGIC" + Colors.ENDC)
        i = 1
        for spell in self.magic:
            print("    " + str(i) + ": " + spell.name + " (cost: " + str(spell.cost) + ")")
            i += 1

    def choose_items(self):
        print(Colors.OKGREEN + "ITEMS" + Colors.ENDC)
        i = 1
        for item in self.items:
            print("    " + str(i) + ": " + item["name"].name, item["name"].description, "(x" + str(item["quantity"]) +")")
            i += 1

    def choose_target(self, enemies):
        print(Colors.FAIL + "TARGETS" + Colors.ENDC)
        i = 1
        for enemy in enemies:
            print("    " + str(i) + ": " + enemy.name)
            i += 1
        index = int(input("Choose your enemy: ")) - 1
        return enemies[index]

    def print_info(self, type_person):
        hp_bars = ""
        hp_bar_numbers = (self.hp / self.maxhp) * 25
        i = 0
        while i < hp_bar_numbers:
            hp_bars += "="
            i += 1

        while hp_bar_numbers < 25 - 1:
            hp_bars += " "
            hp_bar_numbers += 1

        mp_bars = ""
        mp_bar_numbers = self.mp / self.maxmp * 10
        i = 0
        while i < mp_bar_numbers:
            mp_bars += "="
            i += 1

        while mp_bar_numbers < 10 - 1:
            mp_bars += " "
            mp_bar_numbers += 1

        color = Colors.OKGREEN
        if type_person == "enemy":
            color = Colors.FAIL

        hp_result = str(self.hp) + "/" + str(self.maxhp)
        while len(hp_result) < 7:
            hp_result += " "
        mp_result = str(self.mp) + "/" + str(self.maxmp)
        while len(mp_result) < 5:
            mp_result += " "
        print("                " + "         _________________________   " + "        __________")
        print(self.name + "         " + Colors.BOLD + hp_result + " |" + Colors.ENDC +
              color + hp_bars + Colors.ENDC + "|   " +
              Colors.BOLD + mp_result + " |" + Colors.OKBLUE + mp_bars + Colors.ENDC + "|")
