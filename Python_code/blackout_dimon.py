from copy import deepcopy

class DisjointSet:
    def __init__(self, collection):
        self.parent = {}
        self.rank = {}
        for i in collection:
            self.parent[i] = i
            self.rank[i] = 1

    def find(self, k):
        if self.parent[k] != k:
            self.parent[k] = self.find(self.parent[k])
        return self.parent[k]

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)

        if x == y:
            return

        if self.rank[x] > self.rank[y]:
            self.parent[y] = x

        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y

        else:
            self.parent[x] = y
            self.rank[y] += self.rank[x]
    
def kruskal(edges, disset):
    global nvertices
    mst = set()
    mst_ver = set()
    total_cost = 0
    for edge in edges:
        u, v, cost = edge
        if disset.find(u) != disset.find(v):
            mst.add(edge)
            disset.union(u,v)
            total_cost += cost
            if u not in mst_ver:
                mst_ver.add(u)
            if v not in mst_ver:
                mst_ver.add(v)
    if len(mst_ver) != nvertices:
        return mst, float('inf')
    return mst, total_cost

nvertices, nedges = [int(el) for el in input().split()]
edges = []
vertices = set()
for i in range(nedges):
    u,v,cost = [int(el) for el in input().split()]
    if u not in vertices:
        vertices.add(u)
    if v not in vertices:
        vertices.add(v)
    edges.append((u,v,cost))
edges.sort(key=lambda x: x[2])

disset = DisjointSet(vertices)
sample_disset = deepcopy(disset)
mst, first = kruskal(edges, disset)
second = float('inf')
for edge in mst:
    temp_edges = deepcopy(edges)
    edges.remove(edge)
    new_disset = deepcopy(sample_disset)
    second = min(second, kruskal(edges, new_disset)[1])
    edges = deepcopy(temp_edges)
print(first, second)