from characters import Character
from actions import action
from functions import clear_terminal

def main():
    clear_terminal()
    response = input("Start Game? (y/n): ").lower()

    if response == "y":
        name = input("Give your hero a name: ")
        hero = Character(name, 5, 10)
        print(f"Your hero is called {hero.name}!\n")
        input("Press Enter to continue...")
        action(hero)
    elif response == "n":
        print("Until next time!")
    else:
        print("Invalid response!")

if __name__ == "__main__":
    main()
