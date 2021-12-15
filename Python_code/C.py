# Minimum cost of addition
import heapq


def minimum_cost(numbers: list) -> int:
    heapq.heapify(numbers)
    heap_length = len(numbers)
    total_cost = 0
    while heap_length > 1:
        cost = heapq.heappop(numbers) + heapq.heappop(numbers)
        total_cost += cost
        heapq.heappush(numbers, cost)
        heap_length -= 1
    return total_cost


n = int(input())
array = list(map(int, input().split()))
print(minimum_cost(array))
