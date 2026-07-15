import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = int(max_damage)

    def attack(self):
        return random.randint(0, self.max_damage)


if __name__ == "__main__":
    fireball = Ability("Fireball", 50)
    print(fireball.attack())