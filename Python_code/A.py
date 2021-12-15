# Planting trees problem

def party_asap(trees: list) -> int:
    greedy = sorted(trees, reverse=True)
    current_max = 1
    for idx, tree in enumerate(greedy):
        time = tree + idx + 1
        if time > current_max:
            current_max = time
    return current_max + 1


n_trees = int(input())
trees_input = list(map(int, input().split()))
print(party_asap(trees_input))
