# https://leetcode.com/problems/unique-paths/description/
# https://grok.com/chat/453dd434-586d-409c-ae39-16d0fca41228


def uniquePaths(m: int, n: int) -> int:
    # Create a 2D DP array initialized with 0s
    dp = [[0] * n for _ in range(m)]

    # Fill first row and column with 1s since there's only one way
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    # Fill the dp array
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


print(uniquePaths(3, 7))
print(uniquePaths(3, 2))
