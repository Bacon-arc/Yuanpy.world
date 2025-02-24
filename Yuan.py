import random
import os

# print(random.randint(1,100))

equipped = "STICK"
armor = "NOTHING"
inventory = ["STICK"]
gold = 0
spells = []
maxhealth = 10
health = maxhealth
level = 1
exp = 0
explvlup = 25
playerdamage = 2
area = "FOREST"
defense = 1
playerdamagemod = 1
weapons = "STICK, WORN DAGGER"


def loot():
    global gold
    global exp
    global explvlup
    global level
    global health
    global playerdamage
    global maxhealth
    global golddrops
    global itemdrops
    global expdrops
    global defense
    golddrops = 0
    expdrops = 0
    itemdrops = []
    if 'GOBLIN' in enemy1:
        goblinloot()
    if 'GOBLIN' in enemy2:
        goblinloot()
    if 'GOBLIN' in enemy3:
        goblinloot()
    print("Obtained:\n")
    print(f"{expdrops} experience")
    print(f"{golddrops} gold")
    if itemdrops != []:
        print(itemdrops)
    gold += golddrops
    exp += expdrops
    if exp >= explvlup:
        expexcess = exp - explvlup
        exp = expexcess
        print(f"\n{name} leveled up!\n")
        level += 1
        playerdamage += 1
        maxhealth += 5
        health = maxhealth
        defense += 1
        explvlup = round(explvlup * 1.5, 0)
        explvlup = int(explvlup)

def goblincombat():
    global defense
    global health
    enemyattack = random.randint(3, 4) - defense
    if enemyattack > 0:
        print(f"{attackingenemy} strikes {name} for {enemyattack} damage!\n")
        health -= enemyattack
    else:
        print(f"{attackingenemy} strikes, but it bounces off!")


def goblinloot():
    global inventory
    global golddrops
    global itemdrops
    global expdrops
    golddrops += random.randint(2, 3)
    expdrops += 5
    chance = random.randint(1, 10)
    if chance == 10:
        itemdrops.append("RAGGED CLOTH")
        inventory.append("RAGGED CLOTH")
    chance = random.randint(1, 10)
    if chance == 10:
        itemdrops.append("WORN DAGGER")
        inventory.append("WORN DAGGER")

def enemyturn():
    global attackingenemy
    global health
    global maxhealth
    if enemy1hp <= 0 and enemy2hp <= 0 and enemy3hp <= 0:
        print(f"{name} is victorious!\n\nResting...\n")
        health = maxhealth
        loot()
        menu()
    else:
        if enemy1hp > 0:
            if enemy1 == "GOBLIN":
                attackingenemy = enemy1
                goblincombat()
        if enemy2hp > 0:
            if enemy2 == "GOBLIN" or "GOBLIN2":
                attackingenemy = enemy2
                goblincombat()
        if enemy3hp > 0:
            if enemy3 == "GOBLIN" or "GOBLIN2" or "GOBLIN3":
                attackingenemy = enemy3
                goblincombat()

    if health > 0:
        playerturn()
    else:
        print(f"{name} has lost all their hp!\nRetreating...")
        health = maxhealth
        menu()


def setmaxhpenemy():
    global enemymaxhp
    if enemy == "":
        enemymaxhp = 0
    if enemy == "GOBLIN":
        enemymaxhp = 3


def fightstart():
    global enemy1hp
    global enemy2hp
    global enemy3hp
    global enemy1max
    global enemy2max
    global enemy3max
    global enemy
    enemy = enemy1
    setmaxhpenemy()
    enemy1max = enemymaxhp
    enemy1hp = enemymaxhp
    enemy = enemy2
    setmaxhpenemy()
    enemy2max = enemymaxhp
    enemy2hp = enemymaxhp
    enemy = enemy3
    setmaxhpenemy()
    enemy3max = enemymaxhp
    enemy3hp = enemymaxhp
    print("Encountered enemies!\n")
    playerturn()


def playerturn():
    global enemy1
    global enemy2
    global enemy3
    global enemy1hp
    global enemy2hp
    global enemy3hp
    global enemy1max
    global enemy2max
    global enemy3max
    global playerdamagemod
    global playerdamage
    print("Enemies:\n")
    if enemy1hp > 0:
        print(f"{enemy1}, {enemy1hp}/{enemy1max}HP\n")
    if enemy2hp > 0:
        if enemy2 == enemy1:
            enemy2 = f"{enemy2}2"
            print(f"{enemy2}, {enemy2hp}/{enemy2max}HP\n")
        else:
            print(f"{enemy2}, {enemy2hp}/{enemy2max}HP\n")
    if enemy3hp > 0:
        if enemy3 == enemy1 and enemy3 != f"{enemy1}3":
            enemy3 = f"{enemy3}2"
            if enemy3 == enemy2:
                enemy3 = f"{enemy1}3"
                print(f"{enemy3}, {enemy3hp}/{enemy3max}HP\n")
        else:
            print(f"{enemy3}, {enemy3hp}/{enemy3max}HP\n")
    print(f"\n{name} has {health}/{maxhealth}HP\n")
    answer = input("Options: [1] whack/slash/stab enemy, [(designated chant)] cast spell ").upper()
    if answer == "1":
        answer = input(f"Options: [1] return, [Enemy name] target an enemy (not case sensitive) ").upper()
        if answer == enemy1 and enemy1hp > 0:
            clear()
            print(f"{name} strikes {enemy1} for {playerdamage + playerdamagemod} damage!\n")
            enemy1hp -= playerdamage + playerdamagemod
            if enemy1hp <= 0:
                print(f"{enemy1} is defeated!\n")
            enemyturn()
        if answer == enemy2 and enemy2hp > 0:
            clear()
            print(f"{name} strikes {enemy2} for {playerdamage + playerdamagemod} damage!\n")
            enemy2hp -= playerdamage + playerdamagemod
            if enemy2hp <= 0:
                print(f"{enemy2} is defeated!\n")
            enemyturn()
        if answer == enemy3 and enemy3hp > 0:
            clear()
            print(f"{name} strikes {enemy3} for {playerdamage + playerdamagemod} damage!\n")
            enemy3hp -= playerdamage + playerdamagemod
            if enemy3hp <= 0:
                print(f"{enemy3} is defeated!\n")
            enemyturn()
        if answer == "1":
            clear()
            print("\nReturning...\n")
            playerturn()
        else:
            clear()
            print(f"\n{answer} is not a valid option\n")
            playerturn()
    else:
        clear()
        print(f"\n{answer} is not a valid option\n")
        playerturn()


def explore():
    global enemy1
    global enemy2
    global enemy3
    global encounter
    print("\nSetting out...\n")
    if area == "FOREST":
        encounter = random.randint(1, 100)
        if encounter <= 100:
            enemy1 = "GOBLIN"
            enemy2 = "GOBLIN"
            enemy3 = "GOBLIN"
            fightstart()


def checkspells():
    if spells == []:
        clear()
        print("You have no spells!")
        menu()
    else:
        print("\nSpells include:\n")
        print(spells)
        answer = input("\nOptions are: [1] close spell list, [2] inspect spell\n")


def status():
    print(f"\nPlayer: {name}\n")
    print(f"Current health: {health}/{maxhealth}\n")
    print(f"Level: {level}\n")
    print(f"Exp: {exp}/{explvlup}\n")
    print(f"Gold: {gold}\n")
    print(f"Weapon: {equipped}\n")
    print(f"Armor: {armor}\n")
    print(f"Location: {area}\n")
    answer = input("[1] to close ")
    if answer == "1":
        clear()
        print("\nClosing status tab")
        menu()
    else:
        clear()
        print("There was one option given that was a character long. How did you mess that up?")
        status()


def menu():
    answer = input("\nOptions are: [1] open inventory, [2] check spells, [3] check status, [4] explore ").upper()
    if answer == "1":
        clear()
        openinv()
    elif answer == "2":
        clear()
        checkspells()
    elif answer == "3":
        clear()
        status()
    elif answer == "4":
        clear()
        explore()
    else:
        clear()
        print(f"\n{answer} is not an option")
        menu()


def openinv():
    global equipped
    global armor
    print(f"\nYour inventory contains:\n {inventory}\n")
    print(f"You currently have [{equipped}] equipped as a weapon\n")
    print(f"You currently have [{armor}] equipped as armor\n")
    answer = input("Options are: [1] close inventory, [2] inspect item, [3] equip item ")
    if answer == "1":
        clear()
        print("Exiting inventory...\n")
        menu()
    elif answer == "2":
        clear()
        answer = input('Which item? (not case sensitive) ').upper()
        if answer in inventory:
            if answer == 'STICK':
                print('\nDescription of [STICK]:\n')
                print("It's a stick.")
                print("+1 atk. Yeah, that's it.\n")
            if answer == "WORN DAGGER":
                print('\nDescription of [WORN DAGGER]:')
                print('Worn beyond recognition.')
                print('May as well be called an unrefined chunk of iron')
                print('+2 atk.\n')
            if answer == "RAGGED CLOTH":
                print('\nDescription of [RAGGED CLOTH]:\n')
                print('A goblin was wearing this. Just so you know.')
                print('+1 defense, +1 stinkiness')
            openinv()
        else:
            print(f"\nYou don't have anything called {answer}!\n")
            openinv()
    elif answer == "3":
        clear()
        answer = input('Which item? (not case sensitive) ').upper()
        if answer in inventory:
            if answer != equipped and answer != armor:
                if answer in weapons:
                    equipped = answer
                else:
                    armor = answer
                print(f"Equipped [{answer}]!\n")
                openinv()
            else:
                print("\nYou already have this item equipped!\n")
                openinv()
        else:
            print(f"\nYou don't have anything called {answer}!\n")
            openinv()

    else:
        clear()
        print(f"\n{answer} wasn't one of the options last time I checked\n")
        openinv()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()
print("Welcome to Yuanpy.World!\n")

while True:
    name = input("What is your name? ")
    yn = input(f"\nSo your name is {name}? [Y/N] ").upper()
    if yn == 'Y':
        clear()
        print(f'\nRegistered player name: {name}\n')
        print("Loading world...\n")
        break
    else:
        clear()
        print('\nReturning...\n')

print(f"{name} wakes up in a forest with nothing but a stick.\n")
print("If you don't believe me, you should check your inventory and status before setting out")
menu()
