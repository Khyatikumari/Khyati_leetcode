class UF:
    def __init__(self, N):
        self.parent = [i for i in range(N)]

    def find(self, u):
        if self.parent[u] == u:
            return self.parent[u]

        self.parent[u] = self.find(self.parent[u])

        return self.parent[u]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return

        self.parent[pu] = pv

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        N = len(source)

        uf = UF(N)

        for i, j in allowedSwaps:
            uf.union(i, j)
        
        groups = {}
        for i in range(N):
            root = uf.find(i)

            if root not in groups:
                groups[root] = []

            groups[root].append(i)
        
        res = 0
        for key in groups:
            indices = groups[key]

            counter = {}
            for i in indices:
                counter[source[i]] = counter.get(source[i], 0) + 1
            
            for i in indices:
                if counter.get(target[i], 0) > 0:
                    counter[target[i]] -= 1
                else:
                    res += 1
        
        return res