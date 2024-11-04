from player_reader import PlayerReader
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class StatisticsService:
    def __init__(self, player_reader):
        self.player_reader = player_reader
        self._players = player_reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_by=SortBy.POINTS):
        # metodin käyttämä apufufunktio voidaan määritellä näin
        # def sort_by_points(player):
        #     return player.points

        # sorted_players = sorted(
        #     self._players,
        #     reverse=True,
        #     key=sort_by_points
        # )

        # result = []
        # i = 0
        # while i < min(how_many, len(sorted_players)):
        #     result.append(sorted_players[i])
        #     i += 1

        # return result
        if sort_by == SortBy.POINTS:
            key_func = lambda player: player.goals + player.assists
        elif sort_by == SortBy.GOALS:
            key_func = lambda player: player.goals
        elif sort_by == SortBy.ASSISTS:
            key_func = lambda player: player.assists
        else:
            raise ValueError("Unsupported sort type")

        sorted_players = sorted(self._players, key=key_func, reverse=True)
        return sorted_players[:how_many]