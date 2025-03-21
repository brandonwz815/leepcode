from collections import deque

def bfs(graph, start):
  visited = set()
  queue = deque([start])
  visited.add(start)

  while queue:
    node = queue.popleft()

    #  process node
    print(node, end="->")

    for neighbor in graph[node]:
      if neighbor not in visited:
        queue.append(neighbor)
        visited.add(neighbor)

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