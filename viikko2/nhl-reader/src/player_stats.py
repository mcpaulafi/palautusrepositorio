from player import Player

class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nat):
        filtered_players = [player for player in self.players if player['nationality'] == nat]
        sorted_players = sorted(filtered_players, key=lambda player: (player['goals'], player['assists']), reverse=True)
        player_list = []
        for p in sorted_players:
            p_row = Player(p)
            player_list.append(p_row)

        return player_list