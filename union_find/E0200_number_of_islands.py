# https://leetcode.com/problems/number-of-islands/description/
# https://grok.com/chat/5e739228-c431-469b-95e3-41c94972fec9


def numIslands(grid):
    if not grid:
        return 0

    # Initialize variables
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    parent = {}
    count = 0

    # Initialize parent dictionary for all land cells
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1":
                parent[(i, j)] = (i, j)
                count += 1

    def find(p):
        # Find root parent with path compression
        while p != parent[p]: #Brandon: when p == parent[p], you have reached the root
            
            parent[p] = parent[parent[p]]  # Path compression
            p = parent[p]

            # p = parent[parent[p]] #Brandon: get itself or its parent
        return p

    def union(p, q):
        # Union two sets if they're different
        nonlocal count
        rootP = find(p)
        rootQ = find(q)
        if rootP != rootQ:
            parent[rootP] = rootQ
            count -= 1

    # Directions for adjacent cells (right and down only)
    directions = [(0, 1), (1, 0)]

    # Connect adjacent land cells
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1":
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if ni < rows and nj < cols and grid[ni][nj] == "1":
                        union((i, j), (ni, nj))

    return count


# Test cases
grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
print(numIslands(grid1))  # Output: 1

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
print(numIslands(grid2))  # Output: 3
