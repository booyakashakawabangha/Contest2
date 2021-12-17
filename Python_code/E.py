# ACM Contest and Blackout

def two_cheapest(graph: dict) -> tuple:
    first = second = 0
    connected = set()

    return first, second


n, m = list(map(int, input().split()))
graph = [[10 ** 9 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    start, end, cost = list(map(int, input().split()))
    graph[start - 1][end - 1] = cost
    graph[end - 1][start - 1] = cost


seen = [False for _ in range(n)]
min_edge_from = [10 ** 9 for _ in range(n)]
min_edge_outer = [-1 for _ in range(n)]
min_edge_from[0] = 0
helper = []
first = second = 0
for _ in range(n):
    vert = -1
    for j in range(n):
        if not seen[j] and (min_edge_from[j] < min_edge_from[vert] or vert < 0):
            vert = j
    seen[vert] = True

    for k in range(n):
        if graph[vert][k] < min_edge_from[k]:
            min_edge_from[k] = graph[vert][k]
            min_edge_outer[k] = vert
    print(_, seen, min_edge_from, min_edge_outer)

print(sum(min_edge_from))
