# The Staircase problem


def dynamic(array, length):
    """For k = 2"""
    if length == 1:
        return array[0]
    if length == 2:
        return array[1]
    return max(
        array[-1] + dynamic(array[:-1], length - 1),
        array[-2] + dynamic(array[:-2], length - 2)
    )


n = int(input())
M = [0] + list(map(int, input().split())) + [0]
k = int(input())

for i in range(1, n + 2):
    best = -1000000000000000000
    for j in range(1, k + 1):
        if M[i - j] + M[i] > best and i - j >= 0:
            best = M[i - j] + M[i]
    M[i] = best

print(M[-1])
