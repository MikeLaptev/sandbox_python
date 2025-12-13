# -*- coding: utf-8 -*-
from books.python_design_patterns.misc.labels import *


class TennisGame:

    POINTS_SCORE = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def __init__(self, player1_name: str, player2_name: str) -> None:
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1_score()
        else:
            self.p2_score()

    def score(self):
        if self.p1points == self.p2points and self.p1points > 2:
            return DEUCE
        elif self.p1points == self.p2points and self.p1points < 3:
            return f"{TennisGame.POINTS_SCORE[self.p1points]}-{ALL}"

        if (
            self.p1points >= 4
            and self.p2points >= 0
            and (self.p1points - self.p2points) >= 2
        ):
            return f"{WIN_FOR} {self.player1_name}"
        if (
            self.p2points >= 4
            and self.p1points >= 0
            and (self.p2points - self.p1points) >= 2
        ):
            return f"{WIN_FOR} {self.player2_name}"

        if self.p1points > self.p2points >= 3:
            return f"{ADVANTAGE} {self.player1_name}"

        if self.p2points > self.p1points >= 3:
            return f"{ADVANTAGE} {self.player2_name}"

        if self.p1points > 0 and self.p2points == 0:
            p1res = TennisGame.POINTS_SCORE.get(self.p1points, "")
            p2res = LOVE
            return p1res + "-" + p2res
        if self.p2points > 0 and self.p1points == 0:
            p2res = TennisGame.POINTS_SCORE.get(self.p2points, "")
            p1res = LOVE
            return p1res + "-" + p2res

        p1res = None
        p2res = None
        if self.p2points < self.p1points < 4:
            if self.p1points in [2, 3]:
                p1res = TennisGame.POINTS_SCORE.get(self.p1points)
            if self.p2points in [1, 2]:
                p2res = TennisGame.POINTS_SCORE.get(self.p2points)
            if not p1res or not p2res:
                raise ValueError(
                    f"unexpected combination of scores; player {self.player1_name} have got {self.p1points} and player {self.player2_name} have got {self.p2points}"
                )
            return p1res + "-" + p2res
        if self.p1points < self.p2points < 4:
            if self.p1points in [1, 2]:
                p1res = TennisGame.POINTS_SCORE.get(self.p1points)
            if self.p2points in [2, 3]:
                p2res = TennisGame.POINTS_SCORE.get(self.p2points)
            if not p1res or not p2res:
                raise ValueError(
                    f"unexpected combination of scores; player {self.player1_name} have got {self.p1points} and player {self.player2_name} have got {self.p2points}"
                )
            return p1res + "-" + p2res

        raise ValueError(
            f"unexpected scenario; player {self.player1_name} have got {self.p1points} and player {self.player2_name} have got {self.p2points}"
        )

    def set_p1_score(self, number):
        for i in range(number):
            self.p1_score()

    def set_p2_score(self, number):
        for i in range(number):
            self.p2_score()

    def p1_score(self):
        self.p1points += 1

    def p2_score(self):
        self.p2points += 1
