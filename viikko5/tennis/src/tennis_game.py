class Player:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def won_point(self, player_name):
        if self.player1.name == player_name:
            self.player1.score += 1
            return
        self.player2.score += 1
        return

    def get_score(self):
        score = ""
        temp_score = 0

        if self.player1.score == self.player2.score:
            if self.player1.score == 0:
                score = "Love-All"
            elif self.player1.score == 1:
                score = "Fifteen-All"
            elif self.player1.score == 2:
                score = "Thirty-All"
            else:
                score = "Deuce"
        elif self.player1.score >= 4 or self.player2.score >= 4:
            minus_result = self.player1.score - self.player2.score

            if minus_result == 1:
                score = "Advantage player1"
            elif minus_result == -1:
                score = "Advantage player2"
            elif minus_result >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.player1.score
                else:
                    score = score + "-"
                    temp_score = self.player2.score

                if temp_score == 0:
                    score = score + "Love"
                elif temp_score == 1:
                    score = score + "Fifteen"
                elif temp_score == 2:
                    score = score + "Thirty"
                elif temp_score == 3:
                    score = score + "Forty"

        return score
