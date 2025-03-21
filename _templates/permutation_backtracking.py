# https://grok.com/chat/e56f1786-3326-43fc-ae09-7b97c7fa576b


def permute(nums):
    def backtrack(curr_perm):
        # Base case: if current permutation is complete
        if len(curr_perm) == len(nums):
            result.append(curr_perm[:])  # Add a copy to results
            return

        # Try each number that hasn't been used yet
        for num in nums:
            if num not in curr_perm:  # Check if number is unused
                curr_perm.append(num)  # Make choice
                backtrack(curr_perm)  # Recurse
                curr_perm.pop()  # Backtrack (undo choice)

    result = []  # Store all permutations
    backtrack([])  # Start with empty permutation
    return result


# Example usage
nums = [1, 2, 3]
permutations = permute(nums)
print(permutations)  # Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]


'''
Compare with dfs traversal of a graph

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

'''