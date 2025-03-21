# https://grok.com/chat/f45f39e6-d026-4310-b8b8-5e7b6914fb3f

from collections import deque


def bfs(graph, start):
    visited = set()

    queue = deque([start])

    visited.add(start)

    while queue:
        vertex = queue.popleft()
        
        print(vertex, end=" ") # Process the vertex (in this case, just printing it)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# Example usage:
if __name__ == "__main__":
    # Sample graph as an adjacency list
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    print("BFS starting from vertex 'A':")
    bfs(graph, "A")
