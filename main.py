import random
import os


# print(random.randint(1,100))


answer = 42
equipped = "STICK"
armor = "NONE"
inventory = ["STICK"]
gold = 0
spells = []
maxhealth = 10
maxmana = 10
mana = maxmana
health = maxhealth
level = 1
exp = 0
explvlup = 20
playerdamage = 2
area = "FOREST"
defense = 1
playerdefensemod = 0
playerdamagemod = 0
eventchance = 0
weapons = (
    "STICK, WORN DAGGER, CORROSIVE ROCK, TWINDAGGERS, BUCKLER, SAVAGE CLAWS, SAWGRASS"
)
done = []
forestwares = {"TWINDAGGERS": 25, "LEATHER TUNIC": 35, "EMBERS": 30}
playersellprices = {
    "STICK": 1,
    "WORN DAGGER": 5,
    "RAGGED CLOTH": 5,
    "CORROSIVE ROCK": 5,
    "TWINDAGGERS": 10,
    "LEATHER TUNIC": 15,
    "BUCKLER": 10,
    "SAVAGE CLAWS": 25,
    "CORROSIVE COAT": 15,
    "SAWGRASS": 40,
}
availableevents = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def forestshop():
    global \
        answer, \
        gold, \
        name, \
        inventory, \
        forestwares, \
        answer2, \
        spells, \
        armor, \
        equipped, \
        dupeitemcounter
    print(f"Inventory contains:\n")
    for things in inventory:
        print(f"{things} sellable for {playersellprices[things]} gold\n")
    print("\nItems for sale:\n")
    for things in forestwares:
        print(f"{things} purchasable for {forestwares[things]} gold\n")
    print(f"\n{name} has {gold} gold\n")
    answer = input(
        "Options are: [1] leave shop, [2] inspect item, [3] buy item, [4] sell individual item, [5] sell all of one item "
    ).upper()
    if answer == "1":
        clear()
        print('"Come again!"\n')
        menu()
    elif answer == "2":
        clear()
        print("Items for sale:\n")
        for things in forestwares:
            print(f"{things} purchasable for {forestwares[things]} gold\n")
        answer = input("Which item? (not case sensitive) ").upper()
        clear()
        if answer in inventory or forestwares:
            itemdescs()
        else:
            print(f"What do you mean {answer}?!\n")
        forestshop()
    elif answer == "3":
        clear()
        print("Items for sale:\n")
        for things in forestwares:
            print(f"{things} purchasable for {forestwares[things]} gold\n")
        answer = input("Which item? (not case sensitive) ").upper()
        if answer in forestwares:
            if gold >= forestwares[answer]:
                clear()
                gold -= forestwares[answer]
                forestwares.pop(answer)
                if answer == "EMBERS":
                    spells.append("EMBERS")
                else:
                    inventory.append(answer)
                print(f"Bought {answer}!\n\n")
            else:
                clear()
                print('"Broke..."\n')
        else:
            clear()
            print(f"{answer} isn't for sale\n")
        forestshop()
    elif answer == "4":
        clear()
        print("Inventory contains:\n")
        for things in inventory:
            print(f"{things} sellable for {playersellprices[things]} gold\n")
        answer = input("Which item? (not case sensitive) ").upper()
        if answer in inventory:
            dupeitemcounter = 0
            for thing in inventory:
                if thing == answer:
                    dupeitemcounter += 1
            if answer == equipped or answer == armor and dupeitemcounter == 1:
                answer2 = input(
                    f'\n"{answer}, hm? You mean the thing you have equipped right now? I can give you {playersellprices[answer]} gold for it." [Y/N] '
                ).upper()
            else:
                answer2 = input(
                    f'\n"{answer}, hm? I can give you {playersellprices[answer]} gold for it." [Y/N] '
                ).upper()
            while answer2 != "Y" and answer2 != "N":
                clear()
                print(f"{answer2} is not a valid option!")
                if answer != equipped and answer != armor:
                    answer2 = input(
                        f'\n"{answer}, hm? I can give you {playersellprices[answer]} gold for it." [Y/N] '
                    ).upper()
                else:
                    answer2 = input(
                        f'\n"{answer}, hm? You mean the thing you have equipped right now? I can give you {playersellprices[answer]} gold for it." [Y/N] '
                    ).upper()
            if answer2 == "Y":
                gold += playersellprices[answer]
                inventory.remove(answer)
                if answer == equipped and answer not in inventory:
                    equipped = "NONE"
                if answer == armor and answer not in inventory:
                    armor = "NONE"
                clear()
                print(f"Sold {answer} for {playersellprices[answer]} gold!\n")
            else:
                clear()
                print("No deal!\n")
        else:
            print(f"You don't have {answer}!\n")
        forestshop()
    elif answer == "5":
        clear()
        print("Inventory contains:\n")
        for things in inventory:
            print(f"{things} sellable for {playersellprices[things]} gold\n")
        answer = input("Which item? (not case sensitive) ").upper()
        if answer in inventory:
            dupeitemcounter = 0
            for thing in inventory:
                if thing == answer:
                    dupeitemcounter += 1
            if answer == equipped or answer == armor and dupeitemcounter == 1:
                answer2 = input(
                    f'\n"{answer}(s), hm? You mean the thing you have equipped right now? I can give you {playersellprices[answer]} gold for it." [Y/N] '
                ).upper()
            else:
                answer2 = input(
                    f'\n"{answer}(s), hm? I can give you {playersellprices[answer] * dupeitemcounter} gold for all of them." [Y/N] '
                ).upper()
            while answer2 != "Y" and answer2 != "N":
                clear()
                print(f"{answer2} is not a valid option!")
                if answer != equipped and answer != armor:
                    answer2 = input(
                        f'\n"{answer}(s), hm? I can give you {playersellprices[answer] * dupeitemcounter} gold for all of them." [Y/N] '
                    ).upper()
                else:
                    answer2 = input(
                        f'\n"{answer}(s), hm? You mean the thing you have equipped right now? I can give you {playersellprices[answer] * dupeitemcounter} gold for all of them." [Y/N] '
                    ).upper()
            if answer2 == "Y":
                gold += playersellprices[answer] * dupeitemcounter
                for things in inventory:
                    if things == answer:
                        inventory.remove(things)
                if answer == equipped and answer not in inventory:
                    equipped = "NONE"
                if answer == armor and answer not in inventory:
                    armor = "NONE"
                clear()
                print(
                    f"Sold all {answer} for {playersellprices[answer] * dupeitemcounter} gold!\n"
                )
            else:
                clear()
                print("No deal!\n")
        else:
            clear()
            print(f"You don't have {answer}!\n")
        forestshop()
    else:
        clear()
        print(f"{answer} is not a valid option!\n")
        forestshop()


def loot():
    global \
        golddrops, \
        expdrops, \
        itemdrops, \
        gold, \
        exp, \
        level, \
        maxmana, \
        mana, \
        playerdamage, \
        maxhealth, \
        health, \
        explvlup, \
        equipped, \
        armor, \
        inventory, \
        availableevents
    print("Obtained:")
    print(f"{expdrops} experience")
    print(f"{golddrops} gold")
    if enemy1 == "BEAR":
        availableevents.remove(5)
        availableevents.remove(4)
    if enemy1 == "OVERGROWTH":
        availableevents.remove(6)
        availableevents.remove(7)
        availableevents.remove(8)
    if itemdrops != []:
        for things in itemdrops:
            print(things)
            if "[SPELL]" not in things:
                inventory.append(things)
            else:
                things = things.replace("[SPELL]", "")
                spells.append(things)
    gold += golddrops
    exp += expdrops
    if exp >= explvlup:
        expexcess = exp - explvlup
        exp = expexcess
        print(f"\n{name} leveled up!\n")
        level += 1
        maxmana += 5
        mana = maxmana
        playerdamage += 1
        maxhealth += 5
        health = maxhealth
        explvlup *= 2


def slimecombat():
    global attackingenemy, defense, playerdefensemod, health
    enemyattack = random.randint(2, 3) - defense - playerdefensemod
    if attackingenemy == enemy1:
        enemyattack += enemy1attackmod
    if attackingenemy == enemy2:
        enemyattack += enemy2attackmod
    if attackingenemy == enemy3:
        enemyattack += enemy3attackmod
    if enemyattack > 0:
        print(f"{attackingenemy} corrodes {name} for {enemyattack} damage!\n")
        health -= enemyattack
        if armor != "CORROSIVE COAT":
            playerdefensemod -= 1
            print(f"Defense has decreased by 1!\n")
    else:
        print(
            f"{attackingenemy} tries to corrode {name}, but their armor is too thick!\n"
        )
        if armor != "CORROSIVE COAT":
            playerdefensemod -= 1
            print(f"Defense has decreased by 1!\n")


def goblincombat():
    global attackingenemy, defense, playerdefensemod, health
    enemyattack = random.randint(3, 4) - defense - playerdefensemod
    if attackingenemy == enemy1:
        enemyattack += enemy1attackmod
    elif attackingenemy == enemy2:
        enemyattack += enemy2attackmod
    elif attackingenemy == enemy3:
        enemyattack += enemy3attackmod
    if enemyattack > 0:
        print(f"{attackingenemy} strikes {name} for {enemyattack} damage!\n")
        health -= enemyattack
    else:
        print(f"{attackingenemy} strikes, but it bounces off!\n")


def orccombat():
    global \
        attackingenemy, \
        defense, \
        playerdefensemod, \
        health, \
        chance, \
        enemy1defensemod, \
        enemy2defensemod, \
        enemy3defensemod
    chance = random.randint(1, 2)
    if chance == 1:
        enemyattack = random.randint(5, 6) - defense - playerdefensemod
        if attackingenemy == enemy1:
            enemyattack += enemy1attackmod
        elif attackingenemy == enemy2:
            enemyattack += enemy2attackmod
        elif attackingenemy == enemy3:
            enemyattack += enemy3attackmod
        if enemyattack > 0:
            print(f"{attackingenemy} charges at {name} for {enemyattack} damage!\n")
            health -= enemyattack
        else:
            print(f"{attackingenemy} charges at {name} but it barely makes a dent!\n")
    else:
        print(f"{attackingenemy} takes a defensive positon and gains +1 defense!\n")
        if attackingenemy == enemy1:
            enemy1defensemod += 1
        elif attackingenemy == enemy2:
            enemy2defensemod += 1
        elif attackingenemy == enemy3:
            enemy3defensemod += 1


def bigslimecombat():
    global \
        attackingenemy, \
        defense, \
        playerdefensemod, \
        health, \
        chance, \
        enemy1defensemod, \
        enemy2defensemod, \
        enemy3defensemod, \
        statuscount, \
        enemy1statuseffects, \
        enemy2statuseffects, \
        enemy3statuseffects, \
        totalenemyheal, \
        totalenemyburn, \
        spellamp
    if attackingenemyhp >= 10:
        chance = random.randint(1, 1)
        if chance == 1:
            enemyattack = 6 - defense - playerdefensemod
            if attackingenemy == enemy1:
                enemyattack += enemy1attackmod
            elif attackingenemy == enemy2:
                enemyattack += enemy2attackmod
            elif attackingenemy == enemy3:
                enemyattack += enemy3attackmod
            if enemyattack > 0:
                print(f"{attackingenemy} corrodes {name} for {enemyattack} damage!\n")
                health -= enemyattack
            else:
                print(
                    f"{attackingenemy} tries to corrode {name}, but their armor is too thick!\n"
                )
            if armor != "CORROSIVE COAT":
                playerdefensemod -= 1
                print(f"Defense has decreased by 1!\n")
    else:
        statuscount = 0
        if attackingenemy == enemy1:
            enemyattack = 6 - defense - playerdefensemod + enemy1attackmod
            if "6REGEN" not in enemy1statuseffects:
                enemy1statuseffects[f"6REGEN{statuscount}"] = 3
                print(f"{attackingenemy} is starting to reform!")
            elif enemyattack > 0:
                print(f"{attackingenemy} corrodes {name} for {enemyattack} damage!\n")
                health -= enemyattack
                if armor != "CORROSIVE COAT":
                    playerdefensemod -= 1
                    print(f"Defense has decreased by 1!\n")
            else:
                print(
                    f"{attackingenemy} tries to corrode {name}, but their armor is too thick!\n"
                )
                if armor != "CORROSIVE COAT":
                    playerdefensemod -= 1
                    print(f"Defense has decreased by 1!\n")
        elif attackingenemy == enemy2:
            enemyattack = 5 - defense - playerdefensemod + enemy2attackmod
            if "6REGEN" not in enemy2statuseffects:
                enemy2statuseffects[f"6REGEN{statuscount}"] = 3
                print(f"{attackingenemy} is starting to reform!")
            elif enemyattack > 0:
                print(f"{attackingenemy} corrodes {name} for {enemyattack} damage!\n")
                health -= enemyattack
                if armor != "CORROSIVE COAT":
                    playerdefensemod -= 1
                    print(f"Defense has decreased by 1!\n")
            else:
                print(
                    f"{attackingenemy} tries to corrode {name}, but their armor is too thick!\n"
                )
                if armor != "CORROSIVE COAT":
                    playerdefensemod -= 1
                    print(f"Defense has decreased by 1!\n")
        elif attackingenemy == enemy3:
            enemyattack = 5 - defense - playerdefensemod + enemy3attackmod
            if "6REGEN" not in enemy3statuseffects:
                enemy3statuseffects[f"6REGEN"] = 3
                print(f"{attackingenemy} is starting to reform!")
            elif enemyattack > 0:
                print(f"{attackingenemy} corrodes {name} for {enemyattack} damage!\n")
                health -= enemyattack
                if armor != "CORROSIVE COAT":
                    playerdefensemod -= 1
                    print(f"Defense has decreased by 1!\n")
            else:
                print(
                    f"{attackingenemy} tries to corrode {name}, but their armor is too thick!\n"
                )
                if armor != "CORROSIVE COAT":
                    playerdefensemod -= 1
                    print(f"Defense has decreased by 1!\n")


def bearcombat():
    global \
        attackingenemy, \
        defense, \
        playerdefensemod, \
        health, \
        chance, \
        enemy1defensemod, \
        enemy2defensemod, \
        enemy3defensemod
    chance = random.randint(1, 3)
    if chance == 1:
        enemyattack = (
            random.randint(7, 9) - defense - playerdefensemod + enemy1attackmod
        )
        if enemyattack > 0:
            print(f"{attackingenemy} charges at {name} for {enemyattack} damage!\n")
            health -= enemyattack
        else:
            print(f"{attackingenemy} charges at {name}, but barely leaves a dent!\n")
    elif chance == 2:
        enemyattack = 4 + enemy1attackmod
        if enemyattack > 0:
            print(f"{attackingenemy} roars at {name} for {enemyattack} eardamage!\n")
            print(f"{name}'s defense has decreased by 1 due to the intimidation!\n")
            playerdefensemod -= 1
            health -= enemyattack
        else:
            print(f"{attackingenemy} roars, but {name} doesn't flinch!\n")
    elif chance == 3:
        enemyattack = (
            random.randint(4, 6) - defense - playerdefensemod + enemy1attackmod
        )
        if enemyattack > 0:
            print(f"{attackingenemy} swipes at {name} for {enemyattack} damage!\n")
            health -= enemyattack
            print(
                f"{attackingenemy} does a follow up swipe at {name} for {enemyattack} damage!\n"
            )
            health -= enemyattack
        else:
            print(
                f"{attackingenemy} swipes twice at {name}, but it barely leaves a scratch!\n"
            )


def overgrowthcombat():
    global \
        turncount, \
        enemy2statuseffects, \
        enemy3statuseffects, \
        chance, \
        playerstatuseffects, \
        enemy3, \
        attackingenemy, \
        defense, \
        playerdefensemod, \
        health, \
        enemy2, \
        enemy2hp, \
        enemy2max, \
        enemy2attackmod, \
        enemy2defensemod, \
        enemy, \
        enemy3hp, \
        enemy3max, \
        enemy3attackmod, \
        enemy3defensemod, \
        enemy1hp, \
        enemy1max
    if enemy1hp > 0 and enemy1hp < enemy1max:
        enemy1hp += 1
        print(f"OVERGROWTH reforms, healing 1 hp!\n")
    if turncount == 1 or turncount == 8:
        print(f"OVERGROWTH tangles {name}!\n")
        playerstatuseffects["TANGLED"] = 2
    elif enemy2hp < 1 and enemy3hp < 1:
        print("OVERGROWTH summons two VINES!\n")
        enemy2 = "VINE"
        enemy2statuseffects = {}
        enemy = enemy2
        setstatsenemy()
        enemy2max = enemymaxhp
        enemy2hp = enemymaxhp
        enemy2attackmod = enemyattackmod
        enemy2defensemod = enemydefensemod
        enemy = enemy3
        enemy3 = "VINE"
        enemy3statuseffects = {}
        enemy = enemy3
        setstatsenemy()
        enemy3max = enemymaxhp
        enemy3hp = enemymaxhp
        enemy3attackmod = enemyattackmod
        enemy3defensemod = enemydefensemod
        enemy3 = "VINE2"
    else:
        chance = random.randint(1, 4)
        if chance == 1:
            print("OVERGROWTH's vines thrash around!\n")
            enemyattack = 3 - defense - playerdefensemod
            if enemyattack > 0:
                print(f"OVERGROWTH strikes {name} for {enemyattack} damage!\n")
                health -= enemyattack
                print(f"OVERGROWTH strikes {name} for {enemyattack} damage!\n")
                health -= enemyattack
                print(f"OVERGROWTH strikes {name} for {enemyattack} damage!\n")
                health -= enemyattack
            else:
                print(f"OVERGROWTH strikes, but it bounces off!\n")
                print(f"OVERGROWTH strikes, but it bounces off!\n")
                print(f"OVERGROWTH strikes, but it bounces off!\n")
        elif chance == 2 or chance == 3 and enemy2hp < 1 or enemy3hp < 1:
            print("OVERGROWTH transfers magic through its roots!\n")
            print("All VINES gain +1 atk and def!\n")
            enemy2attackmod += 1
            enemy3attackmod += 1
            enemy2defensemod += 1
            enemy3defensemod += 1
        else:
            print(f"OVERGROWTH pierces {name} with one of its vines for 4 damage!\n")
            health -= 4


def vinecombat():
    global attackingenemy, defense, playerdefensemod, health
    enemyattack = 4 - defense - playerdefensemod
    if attackingenemy == enemy1:
        enemyattack += enemy1attackmod
    elif attackingenemy == enemy2:
        enemyattack += enemy2attackmod
    elif attackingenemy == enemy3:
        enemyattack += enemy3attackmod
    if enemyattack > 0:
        print(f"{attackingenemy} lashes at {name} for {enemyattack} damage!\n")
        health -= enemyattack
    else:
        print(f"{attackingenemy} strikes, but it bounces off!\n")


def enemyturn():
    global \
        area, \
        mana, \
        maxmana, \
        looptimes, \
        attackingenemy, \
        enemy1, \
        enemy2, \
        enemy3, \
        health, \
        maxhealth, \
        mana, \
        maxmana, \
        enemy1hp, \
        enemy2hp, \
        enemy3hp, \
        enemy1max, \
        enemy2max, \
        enemy3max, \
        enemy1attackmod, \
        enemy2attackmod, \
        enemy3attackmod, \
        enemy1defensemod, \
        enemy2defensemod, \
        enemy3defensemod, \
        attackingenemyhp, \
        totalenemyheal, \
        enemy1statuseffects, \
        enemy2statuseffects, \
        enemy3statuseffects, \
        totalenemyburn, \
        spellamp
    totalenemyburn = 0
    totalenemyheal = 0
    looptimes = list(enemy1statuseffects.keys())
    for thing in looptimes:
        if "BURN" in thing:
            enemy1statuseffects[thing] -= 1
            spellamp = int(thing[0])
            totalenemyburn += spellamp
            if enemy1statuseffects[thing] == 0:
                enemy1statuseffects.pop(thing)
        if "REGEN" in thing:
            enemy1statuseffects[thing] -= 1
            spellamp = int(thing[0])
            totalenemyheal += spellamp
            if enemy1statuseffects[thing] == 0:
                enemy1statuseffects.pop(thing)
    if totalenemyburn > 0 and enemy1hp > 0:
        print(f"{enemy1} burns for {totalenemyburn} damage!\n")
        enemy1hp -= totalenemyburn
        if enemy1hp <= 0:
            print(f"{enemy1} is defeated!\n")
    if totalenemyheal > 0 and enemy1hp > 0:
        enemy1hp += totalenemyheal
        if enemy1hp > enemy1max:
            enemy1hp = enemy1max
        print(f"{enemy1} regenerates {totalenemyheal} hp!\n")
    totalenemyburn = 0
    totalenemyheal = 0
    looptimes = list(enemy2statuseffects.keys())
    for thing in looptimes:
        if "BURN" in thing:
            enemy2statuseffects[thing] -= 1
            spellamp = int(thing[0])
            totalenemyburn += spellamp
            if enemy2statuseffects[thing] == 0:
                enemy2statuseffects.pop(thing)
        if "REGEN" in thing:
            enemy2statuseffects[thing] -= 1
            spellamp = int(thing[0])
            totalenemyheal += spellamp
            if enemy2statuseffects[thing] == 0:
                enemy2statuseffects.pop(thing)
    if totalenemyburn > 0 and enemy2hp > 0:
        print(f"{enemy2} burns for {totalenemyburn} damage!\n")
        enemy2hp -= totalenemyburn
        if enemy2hp <= 0:
            print(f"{enemy2} is defeated!\n")
    if totalenemyheal > 0 and enemy2hp > 0:
        enemy2hp += totalenemyheal
        if enemy2hp > enemy2max:
            enemy2hp = enemy2max
    totalenemyburn = 0
    totalenemyheal = 0
    looptimes = list(enemy3statuseffects.keys())
    for thing in looptimes:
        if "BURN" in thing:
            enemy3statuseffects[thing] -= 1
            spellamp = int(thing[0])
            totalenemyburn += spellamp
            if enemy3statuseffects[thing] == 0:
                enemy3statuseffects.pop(thing)
        if "REGEN" in thing:
            enemy3statuseffects[thing] -= 1
            spellamp = int(thing[0])
            totalenemyheal += spellamp
            if enemy3statuseffects[thing] == 0:
                enemy3statuseffects.pop(thing)
    if totalenemyburn > 0 and enemy3hp > 0:
        print(f"{enemy3} burns for {totalenemyburn} damage!\n")
        enemy3hp -= totalenemyburn
        if enemy3hp <= 0:
            print(f"{enemy3} is defeated!\n")
    if totalenemyheal > 0 and enemy3hp > 0:
        enemy3hp += totalenemyheal
        if enemy3hp > enemy3max:
            enemy3hp = enemy3max
        print(f"{enemy3} regenerates {totalenemyheal} hp!\n")
        print(f"{enemy2} regenerates {totalenemyheal} hp!\n")
    if enemy1hp <= 0 and enemy2hp <= 0 and enemy3hp <= 0:
        if enemy1 != "OVERGROWTH":
            print(f"{name} is victorious!\n\nHP and MP fully restored!\n")
            health = maxhealth
            mana = maxmana
            loot()
            menu()
        else:
            print(f"{name} cuts through vine after vine, but they just keep coming\n")
            print(f"{name} is victorious!\n\nHP and MP fully restored!\n")
            area = "STRONGHOLD"
            health = maxhealth
            mana = maxmana
            loot()
            menu()
    else:
        if enemy1hp > 0:
            if "TANGLED" in enemy1statuseffects:
                print(f"{enemy1} is immobile!\n")
                enemy1statuseffects["TANGLED"] -= 1
                if enemy1statuseffects["TANGLED"] == 0:
                    enemy1statuseffects.pop("TANGLED")
                    print(f"{enemy1} is no longer tangled!\n")
            else:
                attackingenemy = enemy1
                attackingenemyhp = enemy1hp
                combats()
        if enemy2hp > 0:
            if "TANGLED" in enemy2statuseffects:
                print(f"{enemy2} is immobile!\n")
                enemy2statuseffects["TANGLED"] -= 1
                if enemy2statuseffects["TANGLED"] == 0:
                    enemy2statuseffects.pop("TANGLED")
                    print(f"{enemy2} is no longer tangled!\n")
            else:
                attackingenemy = enemy2
                attackingenemyhp = enemy2hp
                combats()
        if enemy3hp > 0:
            if "TANGLED" in enemy3statuseffects:
                print(f"{enemy3} is immobile!\n")
                enemy3statuseffects["TANGLED"] -= 1
                if enemy3statuseffects["TANGLED"] == 0:
                    enemy3statuseffects.pop("TANGLED")
                    print(f"{enemy3} is no longer tangled!\n")
            else:
                attackingenemy = enemy3
                attackingenemyhp = enemy3hp
                combats()
        if health > 0:
            playerturn()
        else:
            print(f"{name} has lost all their hp!\nRetreating to menu...\n")
            health = maxhealth
            mana = maxmana
            menu()


def combats():
    if (
        attackingenemy == "SLIME"
        or attackingenemy == "SLIME2"
        or attackingenemy == "SLIME3"
    ):
        slimecombat()
    elif (
        attackingenemy == "GOBLIN"
        or attackingenemy == "GOBLIN2"
        or attackingenemy == "GOBLIN3"
    ):
        goblincombat()
    elif (
        attackingenemy == "ORC" or attackingenemy == "ORC2" or attackingenemy == "ORC3"
    ):
        orccombat()
    elif (
        attackingenemy == "BEAR"
        or attackingenemy == "BEAR2"
        or attackingenemy == "BEAR3"
    ):
        bearcombat()
    elif (
        attackingenemy == "BIG SLIME"
        or attackingenemy == "BIG SLIME2"
        or attackingenemy == "BIG SLIME3"
    ):
        bigslimecombat()
    elif (
        attackingenemy == "VINE"
        or attackingenemy == "VINE2"
        or attackingenemy == "VINE3"
    ):
        vinecombat()
    elif (
        attackingenemy == "OVERGROWTH"
        or attackingenemy == "OVERGROWTH2"
        or attackingenemy == "OVERGROWTH3"
    ):
        overgrowthcombat()


def fightstart():
    global \
        tangledused, \
        playerstatuseffects, \
        turncount, \
        golddrops, \
        expdrops, \
        itemdrops, \
        playerdamage, \
        enemy, \
        enemyattackmod, \
        enemydefensemod, \
        enemy1max, \
        enemy1hp, \
        enemy1attackmod, \
        enemy1defensemod, \
        enemy2max, \
        enemy2hp, \
        enemy2attackmod, \
        enemy2defensemod, \
        enemy3max, \
        enemy3hp, \
        enemy3attackmod, \
        enemy3defensemod, \
        enemy1statuseffects, \
        enemy2statuseffects, \
        enemy3statuseffects
    golddrops = 0
    expdrops = 0
    turncount = 0
    itemdrops = []
    tangledused = False
    enemy1statuseffects = {}
    enemy2statuseffects = {}
    enemy3statuseffects = {}
    playerstatuseffects = {}
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


def setstatsenemy():
    global \
        enemy, \
        enemymaxhp, \
        enemyattackmod, \
        enemydefensemod, \
        golddrops, \
        expdrops, \
        itemdrops
    if enemy == "GOBLIN":
        enemymaxhp = 7
        enemyattackmod = 0
        enemydefensemod = 0
        golddrops += random.randint(2, 3)
        expdrops += 5
        chance = random.randint(1, 8)
        if chance == 1:
            itemdrops.append("RAGGED CLOTH")
        chance = random.randint(1, 8)
        if chance == 1:
            itemdrops.append("WORN DAGGER")
    elif enemy == "SLIME":
        enemymaxhp = 5
        enemyattackmod = 0
        enemydefensemod = 0
        golddrops += random.randint(1, 4)
        expdrops += 4
        chance = random.randint(1, 6)
        if chance == 1:
            itemdrops.append("CORROSIVE ROCK")
    elif enemy == "ORC":
        enemymaxhp = 10
        enemyattackmod = 0
        enemydefensemod = 1
        golddrops += random.randint(4, 6)
        expdrops += 9
        chance = random.randint(1, 11)
        if chance == 1:
            itemdrops.append("BUCKLER")
    elif enemy == "BEAR":
        enemymaxhp = 30
        enemyattackmod = 0
        enemydefensemod = 1
        golddrops += 12
        expdrops += 20
        itemdrops.append("SAVAGE CLAWS")
    elif enemy == "BIG SLIME":
        enemymaxhp = 18
        enemyattackmod = 0
        enemydefensemod = 0
        golddrops += random.randint(6, 7)
        expdrops += 10
        chance = random.randint(1, 12)
        if chance == 1:
            itemdrops.append("CORROSIVE COAT")
    elif enemy == "OVERGROWTH":
        enemymaxhp = 55
        enemyattackmod = 0
        enemydefensemod = 0
        golddrops += 50
        expdrops += 100
        itemdrops.append("[SPELL] TANGLE")
        itemdrops.append("SAWGRASS")
    elif enemy == "VINE":
        enemymaxhp = 9
        enemyattackmod = 0
        enemydefensemod = 0
    else:
        enemymaxhp = 0
        enemyattackmod = 0
        enemydefensemod = 0


def itemstats():
    global playerdefensemod, playerdamagemod, equipped
    playerdefensemod = 0
    playerdamagemod = 0
    if equipped == "STICK" or equipped == "CORROSIVE ROCK":
        playerdamagemod += 1
    if equipped == "WORN DAGGER":
        playerdamagemod += 2
    if equipped == "BUCKLER":
        playerdamagemod += 2
        playerdefensemod += 1
    if equipped == "SAVAGE CLAWS":
        playerdamagemod += 4
    if armor == "RAGGED CLOTH":
        playerdefensemod += 1
    if armor == "LEATHER TUNIC":
        playerdefensemod += 2
    if armor == "CORROSIVE COAT":
        playerdefensemod += 5


def playerturn():
    global \
        tangledused, \
        turncount, \
        intmana, \
        playerdefensemod, \
        statuscount, \
        chance, \
        mana, \
        maxmana, \
        name, \
        equipped, \
        enemy, \
        enemy2, \
        enemy3, \
        enemy1max, \
        enemy1hp, \
        enemy1attackmod, \
        enemy1defensemod, \
        enemy2max, \
        enemy2hp, \
        enemy2attackmod, \
        enemy2defensemod, \
        enemy3max, \
        enemy3hp, \
        enemy3attackmod, \
        enemy3defensemod, \
        playerdamagemod
    if armor == "CORROSIVE COAT" and playerdefensemod > 0:
        print("Defense decreased by 1!\n")
        playerdefensemod -= 1
    turncount += 1
    if "TANGLED" not in playerstatuseffects:
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
        print(f"\n{name} has {health}/{maxhealth}HP and {mana}/{maxmana}MP\n")
        answer = input(
            "Options: [1] whack/slash/stab enemy, [2] meditate (regain 40% max mana), [SPELL NAME] cast spell (not case sensitive) "
        ).upper()
        if answer == "1":
            answer = input(
                f"Options: [1] return, [2] target random enemy, [ENEMY NAME] target specific enemy (not case sensitive) "
            ).upper()
            if answer == "2":
                while answer == "2":
                    chance = random.randint(1, 3)
                    if chance == 1 and enemy1hp > 0:
                        answer = enemy1
                    elif chance == 2 and enemy2hp > 0:
                        answer = enemy2
                    elif enemy3hp > 0:
                        answer = enemy3
            if answer == enemy1 and enemy1hp > 0:
                clear()
                if playerdamage + playerdamagemod - enemy1defensemod > 0:
                    print(
                        f"{name} strikes {enemy1} for {playerdamage + playerdamagemod - enemy1defensemod} damage!\n"
                    )
                    enemy1hp -= playerdamage + playerdamagemod - enemy1defensemod
                    if enemy1hp <= 0:
                        print(f"{enemy1} is defeated!\n")
                        if equipped == "SAVAGE CLAWS":
                            print(
                                f"The smell of blood empowers {name}'s attack by 1!\n"
                            )
                            playerdamagemod += 1
                    elif equipped == "CORROSIVE ROCK":
                        print(f"Decreased defense of {enemy1} by 1!\n")
                        enemy1defensemod -= 1
                    elif equipped == "TWINDAGGERS":
                        print(
                            f"{name} does a follow up strike on {enemy1} for {playerdamage + playerdamagemod - enemy1defensemod} damage!\n"
                        )
                        enemy1hp -= playerdamage + playerdamagemod - enemy1defensemod
                    elif equipped == "SAWGRASS":
                        print(
                            f"{name}'s [SAWGRASS] continues to grind into {enemy1} for {playerdamage + playerdamagemod - enemy1defensemod} damage!\n"
                        )
                        enemy1hp -= playerdamage + playerdamagemod - enemy1defensemod
                        print(
                            f"{name}'s [SAWGRASS] continues to grind into {enemy1} for {playerdamage + playerdamagemod - enemy1defensemod} damage!\n"
                        )
                        enemy1hp -= playerdamage + playerdamagemod - enemy1defensemod
                else:
                    print(
                        f"{name} tries to attack {enemy1}, but its defenses are too thick!\n"
                    )
                enemyturn()
            if answer == enemy2 and enemy2hp > 0:
                clear()
                if playerdamage + playerdamagemod - enemy2defensemod > 0:
                    print(
                        f"{name} strikes {enemy2} for {playerdamage + playerdamagemod - enemy2defensemod} damage!\n"
                    )
                    enemy2hp -= playerdamage + playerdamagemod - enemy2defensemod
                    if enemy2hp <= 0:
                        print(f"{enemy2} is defeated!\n")
                        if equipped == "SAVAGE CLAWS":
                            print(
                                f"The smell of blood empowers {name}'s attack by 1!\n"
                            )
                            playerdamagemod += 1
                    elif equipped == "CORROSIVE ROCK":
                        print(f"Decreased defense of {enemy2} by 1!\n")
                        enemy2defensemod -= 1
                    elif equipped == "TWINDAGGERS":
                        print(
                            f"{name} does a follow up strike on {enemy2} for {playerdamage + playerdamagemod - enemy2defensemod} damage!\n"
                        )
                        enemy2hp -= playerdamage + playerdamagemod - enemy2defensemod
                    elif equipped == "SAWGRASS":
                        print(
                            f"{name}'s [SAWGRASS] continues to grind into {enemy2} for {playerdamage + playerdamagemod - enemy2defensemod} damage!\n"
                        )
                        enemy2hp -= playerdamage + playerdamagemod - enemy2defensemod
                        print(
                            f"{name}'s [SAWGRASS] continues to grind into {enemy2} for {playerdamage + playerdamagemod - enemy2defensemod} damage!\n"
                        )
                        enemy2hp -= playerdamage + playerdamagemod - enemy2defensemod
                else:
                    print(
                        f"{name} tries to attack {enemy2}, but its defenses are too thick!\n"
                    )
                enemyturn()
            if answer == enemy3 and enemy3hp > 0:
                clear()
                if playerdamage + playerdamagemod - enemy3defensemod > 0:
                    print(
                        f"{name} strikes {enemy3} for {playerdamage + playerdamagemod - enemy3defensemod} damage!\n"
                    )
                    enemy3hp -= playerdamage + playerdamagemod - enemy3defensemod
                    if enemy3hp <= 0:
                        print(f"{enemy3} is defeated!\n")
                        if equipped == "SAVAGE CLAWS":
                            print(
                                f"The smell of blood empowers {name}'s attack by 1!\n"
                            )
                            playerdamagemod += 1
                    elif equipped == "CORROSIVE ROCK":
                        print(f"Decreased defense of {enemy3} by 1!\n")
                        enemy3defensemod -= 1
                    elif equipped == "TWINDAGGERS":
                        print(
                            f"{name} does a follow up strike on {enemy3} for {playerdamage + playerdamagemod - enemy3defensemod} damage!\n"
                        )
                        enemy3hp -= playerdamage + playerdamagemod - enemy3defensemod
                    elif equipped == "SAWGRASS":
                        print(
                            f"{name}'s [SAWGRASS] continues to grind into {enemy3} for {playerdamage + playerdamagemod - enemy3defensemod} damage!\n"
                        )
                        enemy3hp -= playerdamage + playerdamagemod - enemy3defensemod
                        print(
                            f"{name}'s [SAWGRASS] continues to grind into {enemy3} for {playerdamage + playerdamagemod - enemy3defensemod} damage!\n"
                        )
                        enemy3hp -= playerdamage + playerdamagemod - enemy3defensemod
                else:
                    print(
                        f"{name} tries to attack {enemy3}, but its defenses are too thick!\n"
                    )
                enemyturn()
            if answer == "1":
                clear()
                print("Returning...\n")
                playerturn()
            else:
                clear()
                print(f"{answer} is not a valid option\n")
                playerturn()
        elif answer == "2":
            clear()
            intmana = round(maxmana / 2.5, 0)
            intmana = int(intmana)
            mana += intmana
            if mana > maxmana:
                mana = maxmana
            print(f"{name} restored {intmana} mana!\n")
            enemyturn()
        elif answer in spells:
            if answer == "EMBERS":
                clear()
                statuscount = 0
                if mana >= 6:
                    mana -= 6
                    for things in enemy1statuseffects:
                        if "3BURN" in things:
                            statuscount += 1
                    print(f"{name} casts [EMBERS]. All enemies are on fire!\n")
                    enemy1statuseffects[f"3BURN{statuscount}"] = level
                    statuscount = 0
                    for things in enemy2statuseffects:
                        if "3BURN" in things:
                            statuscount += 1
                    enemy2statuseffects[f"3BURN{statuscount}"] = level
                    statuscount = 0
                    for things in enemy3statuseffects:
                        if "3BURN" in things:
                            statuscount += 1
                    enemy3statuseffects[f"3BURN{statuscount}"] = level
                    enemyturn()
                else:
                    print(f"{name} doesn't have enough mana!\n")
                    playerturn()
            elif answer == "TANGLE":
                if tangledused == False:
                    answer = input(
                        f"Options: [1] return, [2] target random enemy, [ENEMY NAME] target specific enemy (not case sensitive) "
                    ).upper()
                    if answer == "1":
                        clear()
                        print("Returning...\n")
                        playerturn()
                    elif answer == "2":
                        while answer == "2":
                            chance = random.randint(1, 3)
                            if chance == 1 and enemy1hp > 0:
                                answer = enemy1
                            elif chance == 2 and enemy2hp > 0:
                                answer = enemy2
                            elif enemy3hp > 0:
                                answer = enemy3
                    if answer == enemy1 and enemy1hp > 0:
                        clear()
                        if mana >= 20:
                            mana -= 20
                            print(f"{name} casts [TANGLE] on {enemy1}!\n")
                            enemy1statuseffects["TANGLED"] = 3
                            enemyturn()
                        else:
                            print(f"{name} doesn't have enough mana!\n")
                            playerturn()
                        tangledused = True
                    elif answer == enemy2 and enemy2hp > 0:
                        clear()
                        if mana >= 20:
                            mana -= 20
                            print(f"{name} casts [TANGLE] on {enemy2}!\n")
                            enemy2statuseffects["TANGLED"] = 3
                            enemyturn()
                        else:
                            print(f"{name} doesn't have enough mana!\n")
                            playerturn()
                        tangledused = True
                    elif answer == enemy3 and enemy3hp > 0:
                        clear()
                        if mana >= 20:
                            mana -= 20
                            print(f"{name} casts [TANGLE] on {enemy3}!\n")
                            enemy3statuseffects["TANGLED"] = 3
                            enemyturn()
                        else:
                            print(f"{name} doesn't have enough mana!\n")
                            playerturn()
                        tangledused = True
                    else:
                        clear()
                        print(f"{answer} is not a valid option\n")
                        playerturn()
                else:
                    print(f"[TANGLE]'s uses have been exhausted!\n")
                    playerturn()
        elif answer == "KILLALL":
            clear()
            enemy1hp = 0
            enemy2hp = 0
            enemy3hp = 0
            enemyturn()
        else:
            clear()
            print(f"{answer} is not a valid option\n")
            playerturn()
    else:
        print(f"{name} is immobile!\n")
        playerstatuseffects["TANGLED"] -= 1
        if playerstatuseffects["TANGLED"] == 0:
            playerstatuseffects.pop("TANGLED")
        enemyturn()


def explore():
    global enemy1, enemy2, enemy3, area, eventchance, encounter, level, event
    eventchance += 2
    enemy1 = ""
    enemy2 = ""
    enemy3 = ""
    print("Setting out...\n")
    if area == "FOREST":
        encounter = random.randint(eventchance, 8)
        if encounter != 8:
            if level == 1:
                encounter = random.randint(1, 2)
                if encounter == 1:
                    enemy1 = "SLIME"
                else:
                    enemy1 = "GOBLIN"
            elif level == 2:
                encounter = random.randint(1, 3)
                if encounter == 1:
                    enemy1 = "GOBLIN"
                    enemy2 = "GOBLIN"
                elif encounter == 2:
                    enemy1 = "ORC"
                else:
                    enemy1 = "SLIME"
                    enemy2 = "SLIME"
            elif level == 3:
                encounter = random.randint(1, 3)
                if encounter == 1:
                    enemy1 = "ORC"
                    enemy2 = "SLIME"
                    enemy3 = "SLIME"
                elif encounter == 2:
                    enemy1 = "GOBLIN"
                    enemy2 = "ORC"
                elif encounter == 3:
                    enemy1 = "GOBLIN"
                    enemy2 = "GOBLIN"
                    enemy3 = "GOBLIN"
            elif level == 4:
                encounter = random.randint(1, 3)
                if encounter == 1:
                    enemy1 = "ORC"
                    enemy2 = "BIG SLIME"
                if encounter == 2:
                    enemy1 = "BIG SLIME"
                    enemy2 = "BIG SLIME"
                if encounter == 3:
                    enemy1 = "ORC"
                    enemy2 = "ORC"
                    enemy3 = "GOBLIN"
            elif level >= 5:
                encounter = random.randint(1, 2)
                if encounter == 1:
                    enemy1 = "BIG SLIME"
                    enemy2 = "BIG SLIME"
                    enemy3 = "ORC"
                else:
                    enemy1 = "ORC"
                    enemy2 = "ORC"
                    enemy3 = "BIG SLIME"
            fightstart()
        else:
            eventchance = 0
            forestevents()


def forestevents():
    global \
        name, \
        level, \
        enemy1, \
        enemy2, \
        enemy3, \
        availableevents, \
        event, \
        gold, \
        exp, \
        explvlup, \
        mana, \
        maxmana, \
        playerdamage, \
        maxhealth, \
        health, \
        answer
    event = random.randint(1, 8)
    while event not in availableevents:
        event = random.randint(1, 8)
    if event == 1:
        print(
            f"{name} is walking through the forest when they encounter a caravan stationed between two trees."
        )
        answer = input(
            f'"Adventurer, care to exchange goods?" a voice calls out. [Y/N] '
        ).upper()
        while answer != "Y" and answer != "N":
            clear()
            print(f"{answer} is not a valid option!\n")
            print(
                f"{name} moves past some greenery, finding a clear with a caravan stationed over a meadow of flowers."
            )
            answer = input(
                f'"Adventurer, care to exchange goods?" a voice calls out. [Y/N] '
            ).upper()
        if answer == "N":
            clear()
            print(f"{name} continues on their way.\n")
            menu()
        if answer == "Y":
            clear()
            print(
                f"{name} approaches the caravan and the shopkeeper greets them with a smile.\n"
            )
            print('"What are you looking for today?"\n')
            forestshop()
    elif event == 2 or event == 3:
        print(
            f"{name} is walking through the forest when they spot an old man digging through the bushes."
        )
        answer = input(
            f'"Adventurer, care to help me find some herbs?" the old man asks. [Y/N] '
        ).upper()
        while answer != "Y" and answer != "N":
            clear()
            print(f"{answer} is not a valid option!\n")
            print(
                f"{name} while walking through the forest spots an old man digging through some bushes."
            )
            answer = input(
                f'"Adventurer, care to help me find some herbs?" the old man asks. [Y/N] '
            ).upper()
        if answer == "N":
            clear()
            print(f"{name} continues on their way.\n")
            print("So rude...\n")
            menu()
        if answer == "Y":
            clear()
            print(f"{name} digs through the bushes with the old man.")
            print(f"{name} finds some herbs and gives them to the old man.\n")
            print(
                '"Thank you, kind adventurer. Take this as a token of my gratitude."\n'
            )
            print(f"{name} receives 15 gold!")
            print(f"{name} recieves 15 exp!")
            gold += 15
            exp += 15
            if exp >= explvlup:
                expexcess = exp - explvlup
                exp = expexcess
                print(f"\n{name} leveled up!\n")
                level += 1
                maxmana += 5
                mana = maxmana
                playerdamage += 1
                maxhealth += 5
                health = maxhealth
                explvlup *= 2
            availableevents.remove(2)
            availableevents.remove(3)
            menu()
    elif event == 4 or event == 5:
        if level >= 3:
            print(
                f"It's a cold night, and {name} is having trouble finding a place to set up camp."
            )
            answer = input(
                f"{name} spots a cave in the distance. Should {name} sleep here? [Y/N] "
            ).upper()
            while answer != "Y" and answer != "N":
                clear()
                print(f"{answer} is not a valid option!\n")
                print(
                    f"It's a cold night, and {name} is having trouble finding a place to set up camp."
                )
                answer = input(
                    f"{name} spots a cave in the distance. Should {name} sleep here? [Y/N] "
                ).upper()
            if answer == "Y":
                clear()
                print(f"{name} enters the cave. Two red eyes appear in the darkness.\n")
                print("A bear emerges from the shadows!\n")
                enemy1 = "BEAR"
                fightstart()
            if answer == "N":
                clear()
                print(f"{name} sleeps outside on the cold night.\n")
                menu()
        else:
            forestevents()
    elif event == 6 or event == 7 or event == 8:
        if level >= 5:
            print(
                f"{name} is walking through the endless greenery of the forest, when they spot walls of stone at least eight times as tall as the trees."
            )
            print(
                "There's a large gate on one of its sides, but it seems to be covered in thick vines."
            )
            answer = input("Cut them? [Y/N] ").upper()
            while answer != "Y" and answer != "N":
                clear()
                print(f"{answer} is not a valid option!\n")
                print(
                    f"{name} is walking through the endless greenery of the forest, when they spot walls of stone at least eight times as tall as the trees."
                )
                print(
                    "There's a large gate on one of its sides, but it seems to be covered in thick vines."
                )
                answer = input("Cut them? [Y/N] ").upper()
            if answer == "Y":
                clear()
                print(
                    f"{name} cuts into the vines. To their surprise, the vines don't remain stationary.\n"
                )
                answer = input(
                    "WARNING!!! You cannot go back to this area once you leave. Are you sure you want to progress? [Y/N] "
                ).upper()
                while answer != "Y" and answer != "N":
                    clear()
                    print(
                        f"{name} cuts into the vines. To their surprise, the vines don't remain stationary.\n"
                    )
                    answer = input(
                        "WARNING!!! You cannot go back to this area once you leave. Are you sure you want to progress? [Y/N] "
                    ).upper()
                if answer == "Y":
                    clear()
                    print(
                        f"{name} turns away for a moment, and the vines already seem to have regrown."
                    )
                    print("Even better, they're lurching closer...\n")
                    enemy1 = "OVERGROWTH"
                    fightstart()
                if answer == "N":
                    clear()
                    print(f"{name} decides to leave the overgrowth alone\n")
                    menu
            if answer == "N":
                clear()
                print(f"{name} decides to leave the overgrowth alone\n")
                menu()
        else:
            forestevents()
    elif event == 9 or event == 10:
        if level >= 2:
            print(f"{name} finds a wizard tower in the middle of the forest.")
            print(
                "The tall stone structure has a wooden door for an entrance, but unfortunately it's locked."
            )
            answer = input(f"Should {name} try to pick the lock? [Y/N] ").upper()
        else:
            forestevents()
    elif event == 11:
        print(f"{name} finds a corpse laying by a tree.")
        answer = input(f"Should {name} search it? [Y/N] ").upper()
    elif event == 12:
        print(
            f"{name} finds a large stump with the words 'Bobo's Gambling Stump' carved into it."
        )
        answer = input(f"Should {name} search it? [Y/N] ").upper()
    else:
        forestevents()


def checkspells():
    global spells
    if spells == []:
        print("You have no spells!")
        menu()
    else:
        print("Spells include:\n")
        for things in spells:
            print(things)
        answer = input(
            "\nOptions are: [1] close spell list, [2] inspect spell "
        ).upper()
        if answer == "1":
            clear()
            print("Closing spell list\n")
            menu()
        elif answer == "2":
            clear()
            answer = input("Which spell? (not case sensitive) ").upper()
            if answer in spells:
                clear()
                itemdescs()
                checkspells()
            else:
                clear()
                print(f"You don't have any spells called {answer}!\n")
                checkspells()
        else:
            clear()
            print(f"{answer} isn't one of the provided options\n")
            checkspells()


def status():
    print(f"Level {level} Adventurer\n")
    print(f"Player: {name}\n")
    print(f"Health: {health}/{maxhealth}\n")
    print(f"Mana: {mana}/{maxmana}\n")
    print(f"Exp: {exp}/{explvlup}\n")
    print(f"Gold: {gold}\n")
    print(f"Weapon: {equipped}\n")
    print(f"Armor: {armor}\n")
    print(f"Location: {area}\n")
    answer = input("[1] to close ")
    if answer == "1":
        clear()
        print("Closing status tab")
        menu()
    else:
        clear()
        print(
            "There was one option given that was a character long. How did you mess that up?"
        )
        status()


def menu():
    answer = input(
        "\nOptions are: [1] open inventory, [2] check spells, [3] check status, [4] explore "
    ).upper()
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
    elif answer == "IMTESTER":
        clear()
        tester()
    elif answer == "5":
        clear()
        print("You thought you were being clever, huh?")
        menu()
    else:
        clear()
        print(f"{answer} was never an option")
        menu()


def itemdescs():
    global answer
    if answer == "STICK":
        print("Description of [WEAPON] [STICK]:\n")
        print("It's a stick.")
        print("+1 atk. Yeah, that's it.\n")
    if answer == "WORN DAGGER":
        print("Description of [WEAPON] [WORN DAGGER]:")
        print("Worn beyond recognition.")
        print("May as well be called an unrefined chunk of iron")
        print("+2 atk.\n")
    if answer == "RAGGED CLOTH":
        print("Description of [ARMOR] [RAGGED CLOTH]:\n")
        print("A goblin was wearing this. Just so you know.")
        print("+1 defense, +1 stinkiness\n")
    if answer == "CORROSIVE ROCK":
        print("Description of [WEAPON] [CORROSIVE ROCK]:\n")
        print("The core of the slime you killed...")
        print("Or a rock it was in the middle of digesting.")
        print("Either way, it seems to have developed some kind of acidic coating.")
        print("+1 attack, reduce defense of enemies hit by 1 (stacking)\n")
    if answer == "TWINDAGGERS":
        print("Description of [WEAPON] [TWINDAGGERS]:\n")
        print("Two metal toothpicks...")
        print("Light, but potentially very deadly.")
        print(
            "+0 attack, but each strike hits twice. Beware of high defense enemies!\n"
        )
    if answer == "LEATHER TUNIC":
        print("Description of [ARMOR] [LEATHER TUNIC]:\n")
        print(" A tunic made of leather from an undetermined animal.")
        print("+2 defense\n")
    if answer == "BUCKLER":
        print("Description of [WEAPON] [BUCKLER]:\n")
        print("A *perfectly* round shield just waiting to be chipped.")
        print(
            "The center contains a heavy steel ball, capable of causing immense brain damage on bludgeon (not actually)."
        )
        print("+1 defense, +2 attack\n")
    if answer == "SAVAGE CLAWS":
        print("Description of [WEAPON] [SAVAGE CLAWS]:\n")
        print("The claws of a bear, savagely ripped off.")
        print("+4 attack, gain +1 attack whenever you kill an enemy.\n")
    if answer == "CORROSIVE COAT":
        print("Description of [ARMOR] [CORROSIVE COAT]\n")
        print(
            "A cool jacket coated in a thick, corrosive substance that wards enemy attacks."
        )
        print(
            "The jacket's quite acid-resistant, and is probably made of some kind of stomach lining from a large creature"
        )
        print(
            "The coating slips off as you run around the battlefield, so it must repeatedly be reapplied."
        )
        print(
            "+5 defense, -1 defense at the start of each turn (modifier cannot fall below 0). You are immune to corrosion.\n"
        )
    if answer == "EMBERS":
        print("Description of [SPELL] [EMBERS]:\n")
        print("fire shards of... fire.. on all enemies.")
        print(
            "Inflicts a stacking burn effect on all enemies, dealing 3 armor piercing damage per turn with a duration equal to your level. Costs 6 mana."
        )
    if answer == "SAWGRASS":
        print("Description of [WEAPON] [SAWGRASS]:\n")
        print(
            "Also known as a [GRASSSAW], because it's actually just a chainsaw made out of grass magically-infused to become more solid."
        )
        print(
            "[GRASSSAW] would sound weird though since it uses the letter 's' thrice in a row."
        )
        print("+0 attack, but each hit happens thrice.\n")
    if answer == "TANGLE":
        print("Description of [SPELL] [TANGLE]:\n")
        print(
            "Entangles one enemy, preventing it from moving for 3 turns (once per battle)."
        )
        print("Costs 20 mana.\n")


def openinv():
    global equipped, armor, inventory, weapons, answer
    print(f"Your inventory contains:\n")
    for things in inventory:
        print(f"{things}\n")
    print(f"You currently have [{equipped}] equipped as a weapon\n")
    print(f"You currently have [{armor}] equipped as armor\n")
    print(f"You currently have {gold} gold\n")
    answer = input(
        "Options are: [1] close inventory, [2] inspect item, [3] equip item "
    )
    if answer == "1":
        clear()
        print("Exiting inventory...\n")
        menu()
    elif answer == "2":
        clear()
        print("Inventory contains:\n")
        for things in inventory:
            print(f"{things}\n")
        answer = input("Which item? (not case sensitive) ").upper()
        if answer in inventory:
            clear()
            itemdescs()
            openinv()
        else:
            clear()
            print(f"You don't have anything called {answer}!\n")
            openinv()
    elif answer == "3":
        clear()
        print("Inventory contains:\n")
        for things in inventory:
            print(f"{things}\n")
        answer = input("Which item? (not case sensitive) ").upper()
        if answer in inventory:
            if answer != equipped and answer != armor:
                if answer in weapons:
                    equipped = answer
                else:
                    armor = answer
                clear()
                print(f"Equipped [{answer}]!\n")
                openinv()
            else:
                clear()
                print("You already have this item equipped!\n")
                openinv()
        else:
            clear()
            print(f"You don't have anything called {answer}!\n")
            openinv()
    else:
        clear()
        print(f"{answer} wasn't one of the options last time I checked\n")
        openinv()


def tester():
    global \
        enemyattackmod, \
        enemydefensemod, \
        enemymaxhp, \
        answer, \
        enemy1, \
        enemy2, \
        enemy3, \
        enemy1hp, \
        enemy2hp, \
        enemy3hp, \
        enemy1max, \
        enemy2max, \
        enemy3max, \
        enemy1attackmod, \
        enemy2attackmod, \
        enemy3attackmod, \
        enemy1defensemod, \
        enemy2defensemod, \
        enemy3defensemod, \
        enemy1statuseffects, \
        enemy2statuseffects, \
        enemy3statuseffects, \
        attackingenemy, \
        health, \
        maxhealth, \
        mana, \
        maxmana, \
        gold, \
        inventory, \
        area, \
        level, \
        playerdamage, \
        explvlup, \
        exp
    print(f"Level {level} Adventurer\n")
    print(f"Player: {name}\n")
    print(f"Health: {health}/{maxhealth}\n")
    print(f"Mana: {mana}/{maxmana}\n")
    print(f"Exp: {exp}/{explvlup}\n")
    print(f"Gold: {gold}\n")
    print(f"Weapon: {equipped}\n")
    print(f"Armor: {armor}\n")
    print(f"Location: {area}\n")
    try:
        answer = input(
            "Options are: [1] close, [2] set level, [3] set exp, [4] set gold, [5] gain item, [6] gain spell, [7] set area, [8] fight enemies "
        ).upper()
        if answer == "1":
            clear()
            print("Exiting tester menu...\n")
            menu()
        elif answer == "2":
            clear()
            level = int(input("Set level to: "))
            clear()
            print(f"Level set to {level}!\n")
            playerdamage = level
            maxhealth = 5 * (level + 1)
            health = maxhealth
            maxmana = 5 * (level + 1)
            mana = maxmana
            explvlup = 999999
            exp = 0
            tester()
        elif answer == "3":
            clear()
            exp = int(input("Set exp to: "))
            clear()
            print(f"Exp set to {exp}!\n")
            tester()
        elif answer == "4":
            clear()
            gold = int(input("Set gold to: "))
            clear()
            print(f"Gold set to {gold}!\n")
            tester()
        elif answer == "5":
            clear()
            answer = input("What item? ").upper()
            if answer in playersellprices:
                inventory.append(answer)
                clear()
                print(f"Added {answer} to inventory!\n")
            else:
                clear()
                print(f"{answer} is not a valid item!\n")
            tester()
        elif answer == "6":
            clear()
            answer = input("What spell? ").upper()
            clear()
            if answer == "EMBERS":
                spells.append("EMBERS")
                print(f"Added EMBERS to spell list!\n")
            elif answer == "TANGLE":
                spells.append("TANGLE")
                print(f"Added TANGLE to spell list!\n")
            else:
                print(f"{answer} is not a valid spell!\n")
            tester()
        elif answer == "7":
            clear()
            answer = input("Set area to: ").upper()
            if answer == "FOREST":
                area = f"{answer}"
                clear()
                print(f"Area set to {area}!\n")
            else:
                clear()
                print(
                    "You can't set the area to anything other than the forest until more areas are added!\n"
                )
            tester()
        elif answer == "8":
            clear()
            enemy1 = input("Enemy1 = ").upper()
            enemy2 = input("Enemy2 = ").upper()
            enemy3 = input("Enemy3 = ").upper()
            fightstart()
        else:
            clear()
            print(f"{answer} was never an option")
            tester()
    except ValueError:
        clear()
        print("Try using a number next time\n")
        tester()


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def startsequence():
    global name, answer
    name = input("What is your name? ")
    answer = input(f"\nSo your name is {name}? [Y/N] ").upper()
    while answer != "Y" and answer != "N":
        clear()
        print(f"{answer} is not a valid option!\n")
        name = input("What is your name? ")
        answer = input(f"\nSo your name is {name}? [Y/N] ").upper()
    if answer == "Y":
        clear()
        print(f"Registered player name: {name}\n")
        print("Loading world...\n")
        print(f"{name} wakes up in a forest with nothing but a stick\n")
        print(
            "If you don't believe me, you should check your inventory and status before setting out"
        )
        menu()
    elif answer == "N":
        clear()
        print("Returning...\n")
        startsequence()


clear()
print("Welcome to Yuan.py.World!\n")
startsequence()
