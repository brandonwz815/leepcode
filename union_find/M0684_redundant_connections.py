# https://leetcode.com/problems/redundant-connection/description/
# https://grok.com/chat/aca9d311-1251-4ae3-befb-98af6e0f5d28


class Solution:
    def findRedundantConnection(self, edges):
        parent = list(range(len(edges) + 1))  # 1-indexed nodes, so size is n+1

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for edge in edges:
            u, v = edge
            if find(u) == find(
                v
            ):  # If u and v are already connected, this edge is redundant
                return edge
            union(u, v)  # Otherwise, connect them
        return []
