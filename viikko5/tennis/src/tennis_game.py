def set_score(points):
    if points == 0:
        return "Love"
    elif points == 1:
        return "Fifteen"
    elif points == 2:
        return "Thirty"
    elif points == 3:
        return "Forty"
    return "Deuce"


class Player:
    def __init__(self, name, points=0):
        self.name = name
        self.points = points

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def won_point(self, player_name):
        if self.player1.name == player_name:
            self.player1.points += 1
            return
        self.player2.points += 1
        return

    def get_score(self):
        score = ""
        temp_score = 0

        if self.player1.points == self.player2.points:
            if self.player1.points <2:
                score = set_score(self.player1.points) + "-All"
            else:
                score = "Deuce"
        elif self.player1.points >= 4 or self.player2.points >= 4:
            minus_result = self.player1.points - self.player2.points

            if minus_result == 1:
                score = "Advantage player1"
            elif minus_result == -1:
                score = "Advantage player2"
            elif minus_result >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"
        else:
            score = set_score(self.player1.points) + "-" + set_score(self.player2.points)
            # for i in range(1, 3):
            #     if i == 1:
            #         temp_score = self.player1.points
            #     else:
            #         score = score + "-"
            #         temp_score = self.player2.points

            #     if temp_score == 0:
            #         score = score + "Love"
            #     elif temp_score == 1:
            #         score = score + "Fifteen"
            #     elif temp_score == 2:
            #         score = score + "Thirty"
            #     elif temp_score == 3:
            #         score = score + "Forty"

        return score
