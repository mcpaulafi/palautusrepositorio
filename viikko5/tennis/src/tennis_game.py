class Player:
    def __init__(self, name, points=0):
        self.name = name
        self.points = points

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.score = ""

    def result(self):
        return (self.player1.points - self.player2.points)

    def won_point(self, player_name):
        if self.player1.name == player_name:
            self.player1.points += 1
            return
        self.player2.points += 1
        return

    def set_score(self, points):
        if points == 0:
            return "Love"
        elif points == 1:
            return "Fifteen"
        elif points == 2:
            return "Thirty"
        elif points == 3:
            return "Forty"
        return "Deuce"

    def score_less_than_four(self):
        if self.player1.points == self.player2.points:
            if self.player1.points <=2:
                self.score = self.set_score(self.player1.points) + "-All"
            else:
                self.score = "Deuce"
        else:
            self.score = self.set_score(
                self.player1.points) + "-" + self.set_score(
                self.player2.points)

    def score_after_four(self):
        if self.result() == 1:
            self.score = "Advantage player1"
        elif self.result() == -1:
            self.score = "Advantage player2"
        elif self.result() >= 2:
            self.score = "Win for player1"
        else:
            self.score = "Win for player2"

    def get_score(self):
#        print("POINTS:", self.player1.points, "-", self.player2.points, self.result())
        if self.player1.points < 4 and self.player2.points < 4:
            self.score_less_than_four()
        else:
            self.score_after_four()

        return self.score
