from player_reader import PlayerReader
from enum import Enum


class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3


class StatisticsService:
    def __init__(self, pla_rdr: PlayerReader):
        self._players = pla_rdr.get_players()

    def search(self, name):
        return next((
            player
            for player
            in self._players if name in player.name
        ), None)

    def team(self, team_name: str):
        return list(filter(
            lambda player: player.team == team_name,
            self._players
        ))

    def top(self, how_many: int, basis: Enum = SortBy.POINTS):
        return sorted(
            self._players,
            reverse=True,
            key=lambda player: (
                player.points if basis == SortBy.POINTS
                else (
                    player.goals if basis == SortBy.GOALS
                    else player.assists
                )
            )
        )[:how_many]
