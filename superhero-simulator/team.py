import random


class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                break

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def attack(self, other_team):
        living_heroes = [
            hero for hero in self.heroes if hero.is_alive()
        ]

        living_opponents = [
            hero for hero in other_team.heroes if hero.is_alive()
        ]

        while living_heroes and living_opponents:
            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)

            print(hero.name + " battles " + opponent.name)
            hero.battle(opponent)

            living_heroes = [
                hero for hero in self.heroes if hero.is_alive()
            ]

            living_opponents = [
                hero for hero in other_team.heroes if hero.is_alive()
            ]

    def revive_heroes(self):
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def stats(self):
        for hero in self.heroes:
            print(
                hero.name,
                "- Kills:",
                hero.kills,
                "Deaths:",
                hero.deaths
            )


if __name__ == "__main__":
    from ability import Ability
    from hero import Hero

    team_one = Team("Team One")
    team_two = Team("Team Two")

    hero_one = Hero("Superman")
    hero_two = Hero("Batman")

    hero_one.add_ability(Ability("Laser Eyes", 40))
    hero_two.add_ability(Ability("Batarang", 40))

    team_one.add_hero(hero_one)
    team_two.add_hero(hero_two)

    team_one.attack(team_two)
    team_one.stats()
    team_two.stats()