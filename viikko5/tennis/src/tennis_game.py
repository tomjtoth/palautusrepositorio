class TennisGame:
    def __init__(self, player1_name, player2_name):
        self._players = {}
        self._players[player1_name] = 0
        self._players[player2_name] = 0

    def won_point(self, player_name):
        self._players[player_name] += 1

    def _score_eq(self, points):
        names = "Love-All,Fifteen-All,Thirty-All".split(",")
        return names[points] if points in range(3) else "Deuce"

    def _score_gt4(self, player1, player2, points1, points2):
        minus_result = points1 - points2

        if minus_result == 1:
            return "Advantage " + player1
        if minus_result == -1:
            return "Advantage " + player2
        if minus_result >= 2:
            return "Win for " + player1

        return "Win for " + player2

    def _score(self, points1, points2):
        names = "Love,Fifteen,Thirty,Forty".split(",")
        return f"{names[points1]}-{names[points2]}"

    def get_score(self):

        dict_iter = iter(self._players.items())
        player1, points1 = next(dict_iter)
        player2, points2 = next(dict_iter)

        if points1 == points2:
            return self._score_eq(points1)

        if points1 >= 4 or points2 >= 4:
            return self._score_gt4(player1, player2, points1, points2)

        return self._score(points1, points2)
