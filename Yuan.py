import random
import os

def globalize():
 global equipped
 global armor
 global inventory
 global gold
 global spells
 global maxhealth
 global health
 global level
 global exp
 global explvlup
 global playerdamage
 global area
 global defense
 global playerdefensemod
 global playerdamagemod
 global weapons
 global golddrops
 global itemdrops
 global expdrops
 global defense
 global attackingenemy
 global enemy1
 global enemy2
 global enemy3
 global enemy1hp
 global enemy2hp
 global enemy3hp
 global enemy1max
 global enemy2max
 global enemy3max
 global enemymaxhp
 global encounter
 global enemy1defensemod
 global enemy2defensemod
 global enemy3defensemod
 global enemy1attackmod
 global enemy2attackmod
 global enemy3attackmod
 global enemyattackmod
 global enemydefensemod


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
playerdefensemod = 0
playerdamagemod = 0
weapons = "STICK, WORN DAGGER"


def loot():
 globalize()
 golddrops = 0
 expdrops = 0
 itemdrops = []
 if enemy1 == "GOBLIN":
     goblinloot()
 if enemy2 == "GOBLIN" or enemy2 == "GOBLIN2":
     goblinloot()
 if enemy3 == "GOBLIN" or enemy3 == "GOBLIN2" or enemy3 == "GOBLIN3":
     goblinloot()
 if enemy1 == "SLIME":
     slimeloot()
 if enemy2 == "SLIME" or enemy2 == "SLIME2":
     slimeloot()
 if enemy3 == "SLIME" or enemy3 == "SLIME2" or enemy3 == "SLIME3":
     slimeloot()
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


def slimecombat():
  globalize()
  enemyattack = random.randint(2,3) - defense - playerdefensemod
  if attackingenemy == enemy1:
	  enemyattack += enemy1attackmod
  if attackingenemy == enemy2:
	  enemyattack += enemy2attackmod
  if attackingenemy == enemy3:
	  enemyattack += enemy3attackmod
  if enemyattack > 0:
      print(f"{attackingenemy} corrodes {name} for {enemyattack} damage!\n")
      health -= enemyattack
  else:
      print(f"{attackingenemy} tries to corrode {name}, but their armor is too thick!")
  playerdefensemod -= 1
  print(f"Defense has decreased by 1!\n")


def goblincombat():
  globalize()
  enemyattack = random.randint(3, 4) - defense - playerdefensemod
  if attackingenemy == enemy1:
	  enemyattack += enemy1attackmod
  if attackingenemy == enemy2:
	  enemyattack += enemy2attackmod
  if attackingenemy == enemy3:
	  enemyattack += enemy3attackmod
  if enemyattack > 0:
      print(f"{attackingenemy} strikes {name} for {enemyattack} damage!\n")
      health -= enemyattack
  else:
      print(f"{attackingenemy} strikes, but it bounces off!")


def slimeloot():
  globalize()
  golddrops += random.randint(1, 4)
  expdrops += 4
  chance = random.randint(1, 20)
  if chance == 10:
      itemdrops.append("CORROSIVE ROCK")
      inventory.append("CORROSIVE ROCK")


def goblinloot():
 globalize()
 golddrops += random.randint(2, 3)
 expdrops += 5
 chance = random.randint(1, 15)
 if chance == 1:
     itemdrops.append("RAGGED CLOTH")
     inventory.append("RAGGED CLOTH")
 chance = random.randint(1, 15)
 if chance == 1:
     itemdrops.append("WORN DAGGER")
     inventory.append("WORN DAGGER")


def enemyturn():
 globalize()
 if enemy1hp <= 0 and enemy2hp <= 0 and enemy3hp <= 0:
     print(f"{name} is victorious!\n\nResting...\n")
     health = maxhealth
     loot()
     menu()
 else:
     if enemy1hp > 0:
       attackingenemy = enemy1
       if enemy1 == "SLIME":
           slimecombat()
       elif enemy1 == "GOBLIN":
           goblincombat()
     if enemy2hp > 0:
       attackingenemy = enemy2
       if enemy2 == "SLIME" or enemy2 == "SLIME2":
           slimecombat()
       elif enemy2 == "GOBLIN" or enemy2 == "GOBLIN2":
           goblincombat()
     if enemy3hp > 0:
       attackingenemy = enemy3
       if enemy3 == "SLIME" or enemy3 == "SLIME2" or enemy3 == "SLIME3":
           slimecombat()
       elif enemy3 == "GOBLIN" or enemy3 == "GOBLIN2" or enemy3 == "GOBLIN3":
           goblincombat()
 if health > 0:
     playerturn()
 else:
     print(f"{name} has lost all their hp!\nRetreating...")
     health = maxhealth
     menu()


def setstatsenemy():
 globalize()
 if enemy == "":
     enemymaxhp = 0
 if enemy == "GOBLIN":
     enemymaxhp = 7
     enemyattackmod = 0
     enemydefensemod = 0
 if enemy == "SLIME":
     enemymaxhp = 5
     enemyattackmod = 0
     enemydefensemod = 0


def fightstart():
 globalize()
 itemstats()
 enemy = enemy1
 setstatsenemy()
 enemy1max = enemymaxhp
 enemy1hp = enemymaxhp
 enemy1attackmod = enemyattackmod
 enemy1defensemod = enemydefensemod
 enemy = enemy2
 setstatsenemy()
 enemy2max = enemymaxhp
 enemy2hp = enemymaxhp
 enemy2attackmod = enemyattackmod
 enemy2defensemod = enemydefensemod
 enemy = enemy3
 setstatsenemy()
 enemy3max = enemymaxhp
 enemy3hp = enemymaxhp
 enemy3attackmod = enemyattackmod
 enemy3defensemod = enemydefensemod
 print("Encountered enemies!\n")
 playerturn()


def itemstats():
  globalize()
  playerdefensemod = 0
  playerdamagemod = 0
  if equipped == "STICK":
      playerdamagemod = 1
  if equipped == "WORN DAGGER":
      playerdamagemod = 2
  if armor == "RAGGED CLOTH":
      playerdefensemod = 1


def playerturn():
 globalize()
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
     if enemy3 == enemy2:
         enemy3 = f"{enemy3}2"
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
	 if playerdamage + playerdamagemod - enemy1defensemod > 0:
             print(f"\n{name} strikes {enemy1} for {playerdamage + playerdamagemod - enemy1defensemod} damage!\n")
             enemy1hp -= playerdamage + playerdamagemod - enemy1defensemod
	 else:
	     print(f"\n{name} strikes {enemy1}, but its defenses are too thick!")	 
         if enemy1hp <= 0:
             print(f"{enemy1} is defeated!\n")
         enemyturn()
     if answer == enemy2 and enemy2hp > 0:
         clear()
         print(f"\n{name} strikes {enemy2} for {playerdamage + playerdamagemod - enemy2defensemod} damage!\n")
         enemy2hp -= playerdamage + playerdamagemod - enemy2defensemod
         if enemy2hp <= 0:
             print(f"{enemy2} is defeated!\n")
         enemyturn()
     if answer == enemy3 and enemy3hp > 0:
         clear()
         print(f"\n{name} strikes {enemy3} for {playerdamage + playerdamagemod - enemy3defensemod} damage!\n")
         enemy3hp -= playerdamage + playerdamagemod - enemy3defensemod
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
 globalize()
 enemy1 = ""
 enemy2 = ""
 enemy3 = ""
 print("\nSetting out...\n")
 if area == "FOREST":
     encounter = random.randint(1, 100)
     if encounter <= 70:
         if level == 1:
           encounter = random.randint(1,2)
           if encounter == 1:
               enemy1 = "GOBLIN"
           else:
               enemy1 = "SLIME"
         if level == 2:
             encounter = random.randint(1, 3)
             if encounter == 1:
                 enemy1 = "GOBLIN"
                 enemy2 = "SLIME"
             elif encounter == 2:
                 enemy1 = "GOBLIN"
                 enemy2 = "GOBLIN"
             else:
                 enemy1 = "SLIME"
                 enemy2 = "SLIME"
         fightstart()
     else:
         print("You were supposed to get an event but those don't exist yet\n")
         menu()


def checkspells():
 globalize()
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
 globalize()
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

