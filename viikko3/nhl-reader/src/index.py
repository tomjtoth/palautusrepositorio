from textwrap import dedent
import requests
from player import Player


def filter_by_nationality(players: list, nat: str):

    print(
        f"Players from {nat}\n"

        # only python 3.12 allows that linefeed within the f-string, I <3 ~~Python~~ Rust, JS, HTML, CSS, SQL
        + "\n".join([

            str(player) for player in

            filter(
                lambda elem: elem.nationality == nat,
                players
            )
        ])
    )


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    players = [Player(pla) for pla in response]

    filter_by_nationality(players, "FIN")


if __name__ == "__main__":
    main()
