# Chocolate problem

def max_chocos(n_days: int, weight1: int, weight2: int) -> int:
    """
    A function which takes 3 params:
    n_days - number of days to eat chocolate
    heavier - heavier weight
    lighter - lighter weight
    Return max grams of eaten chocolate
    """
    return max(weight1, weight2) * ((n_days + 1) // 2) + \
        min(weight1, weight2) * (n_days // 2)


n, a, b = list(map(int, input().split()))
print(max_chocos(n, a, b))
