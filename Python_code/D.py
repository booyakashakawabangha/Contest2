# Nowruz Cup 2015 


def find_highest(Amanchik_team_score: int, rates: list) -> int:
    sorted_rates = sorted(rates)
    Amanchik_team_score += sorted_rates.pop(-1)
    Amanchik_team_rate = 1
    while sorted_rates:
        current_rate = sorted_rates.pop(0)
        gap = Amanchik_team_score - current_rate
        idx = len(sorted_rates) - 1
        while sorted_rates[idx] > gap and idx >= 0:
            idx -= 1
        current_rate += sorted_rates.pop(idx)
        if current_rate > Amanchik_team_score:
            Amanchik_team_rate += 1
    return Amanchik_team_rate



def find_lowest(Amanchik_team_score: int, rates: list, nteams) -> int:
    sorted_rates = sorted(rates)
    Amanchik_team_score += sorted_rates.pop(0)
    Amanchik_team_rate = nteams
    while sorted_rates:
        current_rate = sorted_rates.pop(-1)
        gap = Amanchik_team_score - current_rate
        idx = len(sorted_rates) - 1
        while sorted_rates[idx] > gap and idx >= 0:
            idx -= 1
        current_rate += sorted_rates.pop(idx)
        if current_rate <= Amanchik_team_score:
            Amanchik_team_rate -= 1
    return Amanchik_team_rate


n = int(input())
rankings = list(map(int, input().split()))
# n = 3
# rankings = [1, 1, 1, 1, 1, 1]
print(find_highest(rankings[0], rankings[1:]),
      find_lowest(rankings[0], rankings[1:], n))
