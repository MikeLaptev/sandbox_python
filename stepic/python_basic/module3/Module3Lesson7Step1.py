# coding=utf-8
__author__ = 'mlaptev'

winner_score = 3
tie_score = 1
loser_score = 0


class TeamStatistic(object):

    def __init__(self, n):
        self.__name = n
        self.__amount_of_games = 0
        self.__wins = 0
        self.__draws = 0
        self.__losses = 0

    @property
    def name(self):
        return self.__name

    @property
    def amout_of_points(self):
        return self.wins*winner_score + self.draws*tie_score + self.losses*loser_score

    @property
    def amount_of_games(self):
        return self.__amount_of_games

    @property
    def wins(self):
        return self.__wins

    def add_win(self):
        self.__wins += 1
        self.__amount_of_games += 1

    @property
    def draws(self):
        return self.__draws

    def add_tie(self):
        self.__draws += 1
        self.__amount_of_games += 1

    @property
    def losses(self):
        return self.__losses

    def add_losses(self):
        self.__losses += 1
        self.__amount_of_games += 1

    def __str__(self):
        return "{}: {} {} {} {} {}".format(self.name,
                                           self.amount_of_games,
                                           self.wins,
                                           self.draws,
                                           self.losses,
                                           self.amout_of_points)


if __name__ == "__main__":
    amount_of_matches = int(input())
    full_statistic = dict()
    for _ in range(amount_of_matches):
        first_team, first_team_score, second_team, second_team_score = input().split(sep=';')
        if first_team not in full_statistic:
            full_statistic[first_team] = TeamStatistic(first_team)
        if second_team not in full_statistic:
            full_statistic[second_team] = TeamStatistic(second_team)
        if first_team_score > second_team_score:
            full_statistic[first_team].add_win()
            full_statistic[second_team].add_losses()
        elif first_team_score == second_team_score:
            full_statistic[first_team].add_tie()
            full_statistic[second_team].add_tie()
        else:
            full_statistic[first_team].add_losses()
            full_statistic[second_team].add_win()
    for name, team_statistic in full_statistic.items():
        print(team_statistic)
