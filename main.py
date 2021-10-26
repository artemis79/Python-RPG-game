from classes.game import *
from classes.magic import Spell
from classes.inventory import Item


print(Colors.FAIL + Colors.BOLD + "An enemy has attacked" + Colors.ENDC)

# Create black spells
fire = Spell("fire", 100, 10, "black")
thunder = Spell("thunder", 100, 10, "black")
blizzard = Spell("blizzard", 100, 10, "black")
meteor = Spell("meteor", 200, 20, "black")
quake = Spell("quake", 140, 14, "black")

# Create white spells
cure = Spell("cure", 100, 10, "white")
cura = Spell("cura", 200, 15, "white")


# Create items
potion = Item("Potion", "potion", "heals 50 hp", 50)
hi_potion = Item("Hi-Potion", "potion", "heals 100 hp", 100)
super_potion = Item("Super-Potion", "potion", "heals 500 hp", 500)
elixir = Item("Elixir", "potion", "restores HP/MP of a party member", 10000)
super_elixir = Item("Super-Elixir", "potion", "restores HP/MP of all party", 10000)

grenade = Item("Grenade", "grenade", "deals 500 damage", 500)


running = True
magic = [fire, thunder, blizzard, meteor, cure, cura]
items = [{"name": potion, "quantity": 15}, {"name": hi_potion, "quantity": 5},
         {"name": super_potion, "quantity": 5}, {"name": elixir, "quantity": 3},
         {"name": super_elixir, "quantity": 2}, {"name": grenade, "quantity": 1}]
player1 = Person("Mahshid", 450, 70, 60, 30, magic, items)
player2 = Person("Mahdi  ", 450, 70, 60, 30, magic, items)
player3 = Person("niki   ", 450, 70, 60, 30, magic, items)

enemy1 = Person("Robot  ", 400, 70, 30, 20, [], [])
enemy2 = Person("Imp    ", 100, 70, 30, 20, [], [])
enemy3 = Person("Imp    ", 200, 70, 30, 20, [], [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]


while running:
    print("Name            " + "HP                                    " + "MP                              ")
    for player in players:
        player.print_info("player")

    print("\n" + Colors.FAIL + "Enemies: " + Colors.ENDC)
    for enemy in enemies:
        enemy.print_info("enemy")

    for player in players:
        print("=================")
        player.choose_action()
        choice = input("Choose your action:")
        index = int(choice) - 1
        if index == -1:
            continue
        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemy.take_damage(dmg)
        elif index == 1:
            player.choose_magic()
            index_magic = int(input("Choose your spell:")) - 1
            spell = player.get_spell(index_magic)
            spell_cost = spell.cost
            spell_dmg = player.generate_spell_damage(index_magic)

            if player.get_mp() < spell_cost:
                print(Colors.FAIL + "You don't have enough mp")
                continue
            player.reduce_mp(spell_cost)

            if spell.type == "black":
                enemy = player.choose_target(enemies)
                enemy.take_damage(spell_dmg)
            elif spell.type == "white":
                player.get_healed(spell_dmg)
        elif index == 2:
            player.choose_items()
            index_item = int(input("Choose your item: ")) - 1
            item = items[index_item]["name"]
            if items[index_item]["quantity"] == 0:
                print(Colors.FAIL + "Non left...")
                continue
            items[index_item]["quantity"] -= 1
            if item.type == "potion":
                player.get_healed(item.prop)
                print("\n" + Colors.OKGREEN + "You have healed: " + str(item.prop) + " HP" + Colors.ENDC)

            elif item.type == "elixir":
                player.hp = player.maxhp
                player.mp = player.maxmp
                print("\n" + Colors.OKGREEN + "Your MP and HP are at max" + Colors.ENDC)

            elif item.type == "grenade":
                enemy = player.choose_target(enemies)
                enemy.take_damage(item.prop)
                print("\n" + Colors.FAIL + "Your enemy has taken " + str(item.prop) + " damage" + Colors.ENDC)

        if enemy.hp == 0:
            enemies.remove(enemy)
        if len(enemies) <= 1:
            print(Colors.OKGREEN + "You have won" + Colors.ENDC)
            running = False
            break
        elif len(players) <= 1:
            print(Colors.FAIL + "You have lost" + Colors.ENDC)
            running = False
            break

    enemy_choice = 1
    dmg = enemy1.generate_damage()
    player1.take_damage(dmg)


