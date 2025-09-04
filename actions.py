import random
import time
from characters import Character
from functions import clear_terminal
from battle import battle

def action(hero):
    while True:
        clear_terminal()
        print("Actions:")
        print("[1] Explore cave")
        print("[2] Rest")
        print("[3] Quit game")

        try:
            choice = int(input("Choose: "))
        except ValueError:
            print("Invalid input!")
            time.sleep(1)
            continue

        if choice == 1:
            explore_cave(hero)
        elif choice == 2:
            print(f"{hero.name} rested!")
            time.sleep(1)
        elif choice == 3:
            print("Exiting game. Bye!")
            break
        else:
            print("Invalid choice!")
            time.sleep(1)

def explore_cave(hero):
    print("Exploring cave...")
    for _ in range(random.randint(3, 6)):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")

    enemy_type = random.choice(["Goblin", "Skeleton"])
    if enemy_type == "Goblin":
        enemy = Character("Goblin", 2, 5)
    else:
        enemy = Character("Skeleton", 3, 7)

    battle(hero, enemy)




