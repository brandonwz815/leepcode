# https://leetcode.com/problems/evaluate-division/description/
# https://grok.com/chat/cacd1ddf-4446-4df6-8e20-c274e647f2c2

from collections import defaultdict


class Solution:
    def calcEquation(self, equations, values, queries):
        # Build the graph
        graph = defaultdict(dict)
        for (x, y), val in zip(equations, values):
            graph[x][y] = val  # x -> y with weight val
            graph[y][x] = 1.0 / val  # y -> x with weight 1/val

        # DFS to find the path and compute the result
        def dfs(start, end, visited):
            # If either node isn't in the graph, no answer
            if start not in graph or end not in graph:
                return -1.0
            # If we found the target, return 1.0 (base case)
            if start == end:
                return 1.0
            visited.add(start)
            # Explore neighbors
            for neighbor, weight in graph[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:  # If we found a valid path
                        return weight * result
            return -1.0

        # Process each query
        results = []
        for start, end in queries:
            results.append(dfs(start, end, set()))
        return results


# Example usage:
equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
solution = Solution()
print(solution.calcEquation(equations, values, queries))
# Output: [6.0, 0.5, -1.0, 1.0, -1.0]

"""
An example of graph looks like:
graph = {
    "a": {"b": 2.0},
    "b": {"a": 0.5, "c": 3.0},
    "c": {"b": 0.333...}
}
"""
