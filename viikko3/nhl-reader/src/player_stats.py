
class PlayerStats:
    def __init__(self, rdr):
        self.stats = rdr

    def top_scorers_by_nationality(self, nat: str) -> list:
        return sorted(
            filter(
                lambda elem: elem.nationality == nat,
                self.stats.players
            ),
            key=lambda pla: pla.goals + pla.assists, reverse=True
        )
