"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    day: int
    bears: list
    fish: list

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        surviving_bears: list[Bear] = []
        for bear in self.bears:
            # help! how do i access age?
            if bear.age <= 5:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        surviving_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)
        self.fish = surviving_fish
        return None

    def remove_fish(self, amount: int):
        count: int = 0
        while count <= amount:
            self.fish.pop(count)
            count += 1
        return None

    def bears_eating(self):
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(amount=3)
                bear.eat(num_fish=amount)
        return None

    def check_hunger(self):
        non_starving_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                non_starving_bears.append(bear)
        self.bears = non_starving_bears
        return None

    # better way to do this?
    def repopulate_fish(self):
        fishpop: int = len(self.fish)
        if fishpop % 2 == 0:
            for fish in self.fish:
                self.fish.append(Fish())
                self.fish.append(Fish())
        if fishpop % 2 == 1:
            fishcount: int = 0
            while fishcount < fishpop:
                self.fish.append(Fish())
                self.fish.append(Fish())
                fishcount += 1
        return None

    def repopulate_bears(self):

        return None

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {self.fish}")
        print(f"Bear population: {self.bears}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        daycount: int = 0
        while daycount < 7:
            # does this work to cycle through?
            self.one_river_day()
            daycount += 1
        return None
