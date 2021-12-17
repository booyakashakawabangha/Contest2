from random import randint
# Platforms problem

"""
def dynamic(array, level, length):
    if length == 1:
        return array[0] - level
    elif length == 2:
        return array[1]  - level
    first = array[1]
    second = array[2]
    return min (
        abs(level - first) + dynamic(array[1:], first, length - 1),
        3 * abs(level - second) + dynamic(array[2:], second, length - 2)
    )
"""

# n = 6
# P = [1, 100, 3, 4, 5, 6]


# n = 5
# P = [1] * n
# for i in range(1, n):
#     P[i] = P[i - 1] + randint(0, 3)
# print(P)
# print()


n = int(input())
P = list(map(int, input().split()))
i = 0
total = 0
length = 0
res = []
while i < n - 1:
    length += 1
    res.append(i + 1)
    best = 100000000000000
    if abs(P[i] - P[i + 1]) < best:
        best = abs(P[i] - P[i + 1])
    if i < n - 2 and 3 * abs(P[i] - P[i + 2]) < best:
        best = 3 * abs(P[i] - P[i + 2])
        i += 1
    total += best
    i += 1
res.append(n)
print(total)
print(length + 1)
print(" ".join(map(str, res)))
