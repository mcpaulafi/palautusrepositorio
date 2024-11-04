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

    def test_search_found(self):
        player = self.stats.search("Kurri")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Kurri")

    def test_search_not_found(self):
        player = self.stats.search("Messier")
        self.assertIsNone(player)

    def test_team_found(self):
        team_players = self.stats.team("EDM")
        self.assertEqual(len(team_players), 3)

    def test_team_not_found(self):
        team_players = self.stats.team("ABC")
        self.assertEqual(len(team_players), 0)

    def test_top_players(self):
        top_players = self.stats.top(3)
        self.assertEqual(len(top_players), 3)

    def test_top_players_request_more_than_exists(self):
        top_players = self.stats.top(10)  # Pyynnössä on enemmän pelaajia kuin listassa on
        self.assertEqual(len(top_players), 5)  # Oletetaan, että alkuperäisessä listassa on 5 pelaajaa

if __name__ == '__main__':
    unittest.main()