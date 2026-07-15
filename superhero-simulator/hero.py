from ability import Ability
from armor import Armor
from weapon import Weapon


class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

        self.abilities = []
        self.armors = []

        self.kills = 0
        self.deaths = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        total_damage = 0

        for ability in self.abilities:
            total_damage += ability.attack()

        return total_damage

    def defend(self):
        total_block = 0

        for armor in self.armors:
            total_block += armor.block()

        return total_block

    def take_damage(self, damage):
        damage_after_defense = damage - self.defend()

        if damage_after_defense < 0:
            damage_after_defense = 0

        self.current_health -= damage_after_defense

    def is_alive(self):
        return self.current_health > 0

    def add_kill(self, number_of_kills=1):
        self.kills += number_of_kills

    def add_death(self, number_of_deaths=1):
        self.deaths += number_of_deaths

    def battle(self, opponent):
        if len(self.abilities) == 0 or len(opponent.abilities) == 0:
            print("Draw")
            return

        while self.is_alive() and opponent.is_alive():
            opponent.take_damage(self.attack())

            if not opponent.is_alive():
                print(self.name + " won!")
                self.add_kill()
                opponent.add_death()
                break

            self.take_damage(opponent.attack())

            if not self.is_alive():
                print(opponent.name + " won!")
                opponent.add_kill()
                self.add_death()
                break


if __name__ == "__main__":
    hero_one = Hero("Grace Hopper", 100)
    hero_two = Hero("Superman", 100)

    hero_one.add_ability(Ability("Coding Power", 40))
    hero_two.add_ability(Ability("Laser Eyes", 40))

    hero_one.add_armor(Armor("Computer Shield", 10))
    hero_two.add_armor(Armor("Cape", 10))

    hero_one.battle(hero_two)