from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or
from query_builder import QueryBuilder


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(20, "assists"),
        PlaysIn("PHI")
    )

    matcher = And(
        Not(HasAtLeast(2, "goals")),
        PlaysIn("NYR")
    )

    matcher = And(
        HasFewerThan(2, "goals"),
        PlaysIn("NYR")
    )

    matcher = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    )

    matcher = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    )

    query = QueryBuilder()
    matcher = query \
        .plays_in("NYR") \
        .has_at_least(10, "goals") \
        .has_fewer_than(20, "goals") \
        .build()

    m1 = query \
        .plays_in("PHI") \
        .has_at_least(10, "assists") \
        .has_fewer_than(5, "goals") \
        .build()

    m2 = query \
        .plays_in("EDM") \
        .has_at_least(50, "points") \
        .build()

    matcher = query.one_of(m1, m2).build()

    for player in stats.matches(matcher):
        print(player)

    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))


if __name__ == "__main__":
    main()
