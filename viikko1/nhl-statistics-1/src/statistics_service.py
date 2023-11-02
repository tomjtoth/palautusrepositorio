from player_reader import PlayerReader


class StatisticsService:
    def __init__(self, pla_rdr: PlayerReader):
        self._players = pla_rdr.get_players()

    def search(self, name):
        return next((
            player
            for player
            in self._players if name in player.name
        ), None)

    def team(self, team_name):
        return list(filter(
            lambda player: player.team == team_name,
            self._players
        ))

    def top(self, how_many):
        return sorted(
            self._players,
            reverse=True,
            key=lambda player: player.points
        )[:how_many]
