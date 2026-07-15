import random
from ability import Ability


class Weapon(Ability):
    def attack(self):
        half_damage = self.max_damage // 2
        return random.randint(half_damage, self.max_damage)


if __name__ == "__main__":
    sword = Weapon("Sword", 40)
    print(sword.attack())