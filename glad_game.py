from gladiator import Gladiator
import random
import time
names = ['Maximus', 'Brutus', 'Romulus', 'Remus', 'Aurelius', 'Vulpes']
weapons = ['Spear', 'Sword', 'Knife', 'Mace']


def main():
    print("""
    Welcome to the colloseum!
    Here you will command your champion to fight to the
    death against a gladiator of an opposing nation.
    You may choose your champion's name, weapon, and
    decide what he is to do during the fight.
    Begging for mercy and fleeing are signs of cowardice.
    Begin!
    """)
    begin = input("What is your champion's name? ").strip().lower().capitalize()
    weapon = input("""
    Choose your champion's weapon:
    Spear (7-11 damage)
    Sword (4-13 damage)
    Knife (4-7 damage)
    Mace (9 damage)
    Fists (The Weapons of Real Men) (2-4 damage)
    Enter your choice:
    """).strip().lower().capitalize()
    if weapon == "Spear":
        print("Pointy and stabby. Nice!")
        low = 7
        high = 11
    elif weapon == "Sword":
        print("Boring and original. Fantastic.")
        low = 4
        high = 13
    elif weapon == "Knife":
        print("... I mean, if that's what you want.")
        low = 4
        high = 7
    elif weapon == "Mace":
        print("Who needs a sharp edge, huh?")
        low = 9
        high = 10
    elif weapon == "Fists":
        print("You are a brave soul.")
        low = 2
        high = 4
    else:
        print("Not an option!")
    begin = Gladiator(begin, 100, 0, low, high)
    name = names[random.randint(0, 5)]
    opp_weapon = weapons[random.randint(0, 3)]
    print("Your champion's opponent will be {0}. He will wield a {1}.".format(
        name, opp_weapon))
    if opp_weapon == "Spear":
        opp_low = 7
        opp_high = 11
    elif opp_weapon == "Sword":
        opp_low = 4
        opp_high = 13
    elif opp_weapon == "Knife":
        opp_low = 4
        opp_high = 7
    elif opp_weapon == "Mace":
        opp_low = 9
        opp_high = 10
    name = Gladiator(name, 100, 0, opp_low, opp_high)

    while True:
        dead_check = begin.isDead(name)
        if dead_check == 1:
            print("You have have perished in the fighting pits at the hands of {0}!".format(
                name.name))
            break
        elif dead_check == 2:
            print("You have slain {0} and arise a champion!".format(name.name))
            break
        time.sleep(1)
        choice = input("""
        What would you like your champion to do?
        - Attack
        - Heal
        - Beg
        - Flee
        """).strip().lower().capitalize()
        if choice == "Attack":
            print(begin.attack(name))
        elif choice == "Heal":
            print(begin.heal())
        elif choice == "Beg":
            print(begin.beg())
            break
        elif choice == "Flee":
            print("You are stabbed in the back and die as you flee.")
            break
        print(name.attack(begin))
if __name__ == '__main__':
    main()
