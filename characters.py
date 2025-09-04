import time

class Character:
    def __init__(self, name, damage, life):
        self.name = name
        self.damage = damage
        self.life = life

    def attack(self, enemy):
        print(f"{self.name} attacked {enemy.name}, causing {self.damage} damage!")
        enemy.life -= self.damage

        if enemy.isAlive():
            print(f"{enemy.name} is still alive with {enemy.life} HP!")
        else:
            print(f"{enemy.name} was defeated!")

        time.sleep(1)

    def isAlive(self):
        return self.life > 0
