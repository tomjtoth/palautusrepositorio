import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_returns_as_intended(self):
        self.assertEqual(
            self.stats.search("ret"),
            self.stats._players[4]
        )

    def test_search_returns_None(self):
        self.assertEqual(
            self.stats.search("QQQ"),
            None
        )

    def test_team_works(self):
        self.assertEqual(self.stats.team("EDM"), [
            self.stats._players[0],
            self.stats._players[2],
            self.stats._players[4]
        ])

    def test_top_works(self):
        self.assertEqual(self.stats.top(2), [
            self.stats._players[4],
            self.stats._players[1],
        ])
