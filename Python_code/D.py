from random import randint
# Nowruz Cup 2015


def find_highest(Amanchik_team_score: int, rates: list, n_teams) -> int:
    sorted_rates = sorted(rates)
    Amanchik_team_score += sorted_rates.pop(-1)
    Amanchik_team_rate = 1
    n_teams -= 1
    while n_teams > 0:
        current_score = sorted_rates.pop(0)
        gap = Amanchik_team_score - current_score
        i = 0
        while i < 2 * n_teams - 2 and sorted_rates[i] < gap:
            i += 1
        current_score += sorted_rates.pop(i)
        n_teams -= 1
        if current_score > Amanchik_team_score:
            Amanchik_team_rate += 1
    return Amanchik_team_rate


def find_lowest(Amanchik_team_score: int, rates: list, n_teams) -> int:
    sorted_rates = sorted(rates)
    Amanchik_team_score += sorted_rates.pop(0)
    Amanchik_team_rate = n_teams
    n_teams -= 1
    while n_teams > 0:
        current_score = sorted_rates.pop(-1)
        gap = Amanchik_team_score - current_score
        i = 2 * n_teams - 2
        while i >= 0 and sorted_rates[i] > gap:
            i -= 1
        current_score += sorted_rates.pop(i)
        n_teams -= 1
        if current_score <= Amanchik_team_score:
            Amanchik_team_rate -= 1
    return Amanchik_team_rate


n = int(input())
rankings = list(map(int, input().split()))
# n = 6
# rankings = [randint(0, 5) for i in range(n * 2)]
# n = 5
# rankings = [1, 1, 1, 4, 4, 4, 4, 4, 4, 5]
print(find_highest(rankings[0], rankings[1:], n),
      find_lowest(rankings[0], rankings[1:], n))
