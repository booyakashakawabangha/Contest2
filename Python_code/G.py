# Platforms problem

n = int(input())
P = list(map(int, input().split()))
dynamic = [0 for _ in range(n)]
dynamic[1] = abs(P[1] - P[0])
i = 2
path = [-1, 0] + [-1 for _ in range(n - 2)]
while i < n:
    dynamic[i] = abs(P[i] - P[i - 1]) + dynamic[i - 1]
    path[i] = i - 1
    if 3 * abs(P[i] - P[i - 2]) + dynamic[i - 2] < dynamic[i]:
        path[i] = i - 2
        dynamic[i] = 3 * abs(P[i] - P[i - 2]) + dynamic[i - 2]
    i += 1
print(dynamic[-1])
res = []
temp = n - 1
while temp != 0:
    res.append(temp)
    temp = path[temp]
res.append(0)
length = len(res)
print(length)
print(" ".join(map(str, map(lambda x: x + 1, res[::-1]))))