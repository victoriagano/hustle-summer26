from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team


class Arena:
    def __init__(self):
        self.team_one = Team("Team One")
        self.team_two = Team("Team Two")

    def create_ability(self):
        name = input("What is the ability name? ")
        max_damage = int(input("What is the max damage of the ability? "))

        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("What is the weapon name? ")
        max_damage = int(input("What is the max damage of the weapon? "))

        return Weapon(name, max_damage)

    def create_armor(self):
        name = input("What is the armor name? ")
        max_block = int(input("What is the max block of the armor? "))

        return Armor(name, max_block)

    def create_hero(self):
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)

        add_item = ""

        while add_item != "4":
            add_item = input(
                "[1] Add ability\n"
                "[2] Add weapon\n"
                "[3] Add armor\n"
                "[4] Done adding items\n"
                "Your choice: "
            )

            if add_item == "1":
                ability = self.create_ability()
                hero.add_ability(ability)

            elif add_item == "2":
                weapon = self.create_weapon()
                hero.add_weapon(weapon)

            elif add_item == "3":
                armor = self.create_armor()
                hero.add_armor(armor)

        return hero

    def build_team_one(self):
        number_of_members = int(
            input("How many members would you like on Team One? ")
        )

        for _ in range(number_of_members):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        number_of_members = int(
            input("How many members would you like on Team Two? ")
        )

        for _ in range(number_of_members):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        print("\n" + self.team_one.name + " statistics:")
        self.team_one.stats()

        print("\n" + self.team_two.name + " statistics:")
        self.team_two.stats()

        team_one_kills = sum(hero.kills for hero in self.team_one.heroes)
        team_one_deaths = sum(hero.deaths for hero in self.team_one.heroes)

        team_two_kills = sum(hero.kills for hero in self.team_two.heroes)
        team_two_deaths = sum(hero.deaths for hero in self.team_two.heroes)

        if team_one_deaths == 0:
            team_one_deaths = 1

        if team_two_deaths == 0:
            team_two_deaths = 1

        print(
            "\n" + self.team_one.name + " average K/D:",
            team_one_kills / team_one_deaths
        )

        print(
            self.team_two.name + " average K/D:",
            team_two_kills / team_two_deaths
        )

        team_one_survivors = 0
        team_two_survivors = 0

        print("\nSurvivors:")

        for hero in self.team_one.heroes:
            if hero.is_alive():
                team_one_survivors += 1
                print(hero.name + " survived from " + self.team_one.name)

        for hero in self.team_two.heroes:
            if hero.is_alive():
                team_two_survivors += 1
                print(hero.name + " survived from " + self.team_two.name)

        if team_one_survivors > team_two_survivors:
            print("\n" + self.team_one.name + " wins!")

        elif team_two_survivors > team_one_survivors:
            print("\n" + self.team_two.name + " wins!")

        else:
            print("\nThe battle was a draw!")


if __name__ == "__main__":
    game_is_running = True

    arena = Arena()

    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:
        arena.team_battle()
        arena.show_stats()

        play_again = input("\nPlay again? Y or N: ")

        if play_again.lower() == "n":
            game_is_running = False
        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()