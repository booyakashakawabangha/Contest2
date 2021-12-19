# Ruote 2 problem
from copy import copy

n, k = list(map(int, input().split()))

basic = [list(map(int, input().split())) for _ in range(n)]
dynamic = [[0 for _ in range(n)] for _ in range(n)]
dynamic[0][0] = basic[0][0]
depth, width = 0, 0
maximal = basic[0][0]
directions = set()
directions.add((0, 1))
directions.add((1, 0))
directions.add((0, -1))
directions.add((-1, 0))

next_options = set()
next_options.add((0, 0))

while k > 1:
    options = copy(next_options)

    while options:
        next_options = set()
        depth, width = options.pop()

        for x, y in directions:
            if width < n - 1 and x == 1:
                local_max = max(
                    dynamic[depth][width + 1],
                    basic[depth][width + 1] + dynamic[depth][width]
                )
                dynamic[depth][width + 1] = local_max
                maximal = max(local_max, maximal)
                next_options.add((depth, width + 1))
            
            elif depth < n - 1 and y == 1:
                local_max = max(
                    dynamic[depth + 1][width],
                    basic[depth + 1][width] + dynamic[depth][width]
                )
                dynamic[depth + 1][width] = local_max
                maximal = max(local_max, maximal)
                next_options.add((depth + 1, width))

            elif width > 0 and x == -1:
                local_max = max(
                    dynamic[depth][width - 1],
                    basic[depth][width - 1] + dynamic[depth][width]
                )
                dynamic[depth][width - 1] = local_max
                maximal = max(local_max, maximal)
                next_options.add((depth, width - 1))


            elif depth > 0 and y == -1:
                local_max = max(
                    dynamic[depth - 1][width],
                    basic[depth - 1][width] + dynamic[depth][width]
                )
                dynamic[depth - 1][width] = local_max
                maximal = max(local_max, maximal)
                next_options.add((depth - 1, width))

            
    # print(maximal)
    k -= 1

print(maximal)

"""
4 4
0 0 1 1
15 15 1 1
0 0 1 1
1000 1 1 1
"""
