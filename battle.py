import random
import time
from characters import Character
from functions import clear_terminal

def battle(hero, enemy):
    clear_terminal()
    print(f"{hero.name} found a wild {enemy.name}!\n")

    while hero.isAlive() and enemy.isAlive():
        print(f"What will {hero.name} do?")
        print("[1] Attack")
        print("[2] Try to escape")

        try:
            choice = int(input("Choose: "))
        except ValueError:
            print("Invalid input!")
            continue

        if choice == 1:
            hero.attack(enemy)
            if enemy.isAlive():
                enemy.attack(hero)
            else:
                print("Returning to base...")
                time.sleep(2)
                break
        elif choice == 2:
            escape_chance = random.randint(1,5)
            if escape_chance <= 4:
                print("You managed to escape! Returning to base...")
                time.sleep(2)
                break
            else:
                print(f"Failed to escape! {enemy.name} attacks!")
                enemy.attack(hero)
        else:
            print("Invalid choice!")
