"""Plan a Tea Party for n People"""

__author__: str = "730471503"


def main_planner(guests: int) -> None:
    """Entrypoint of Tea Party Planner"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))


def tea_bags(people: int) -> int:
    """Calculate number of teabags"""
    return 2 * people


def treats(people: int) -> int:
    """Calculate number of treats"""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate cost of tea and treats"""
    return 0.50 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
