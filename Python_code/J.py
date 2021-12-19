# Railway problem

L1, L2, L3, C1, C2, C3 = list(map(int, input().split()))
n = int(input())
init, fin = list(map(int, input().split()))
if init > fin:
    init, fin = fin, init
if fin >= n:
    fin = n
if init == 1:
    road = [0]
else:
    road = []
for i in range(1, n):
    if i in range(init - 1, fin):
        road.append(int(input()))
    else:
        input()

length = fin - init + 1
dynamic = [0] + [1000000000 for _ in range(length - 1)]
for i in range(1, length):
    j = i - 1
    while j >= 0 and road[i] - road[j] <= L3:
        distance = road[i] - road[j]
        if distance > L2:
            cost = C3
        elif distance > L1:
            cost = C2
        else:
            cost = C1

        if cost + dynamic[j] < dynamic[i]:
            dynamic[i] = cost + dynamic[j]
        j -= 1

print(dynamic[-1])
