# https://leetcode.com/problems/unique-paths-ii/description/
# https://grok.com/chat/84e57a0b-150f-4bda-81e1-19e4c6ca6a47


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        # Check if grid is empty or start is blocked
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1  # Starting point has 1 way if not blocked

        # Initialize first row
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[j] = dp[j - 1]
            else:
                dp[j] = 0

        # Process each subsequent row
        for i in range(1, m):
            # Update first column of current row
            if obstacleGrid[i][0] == 1:
                dp[0] = 0
            # Update rest of the row
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[j] = dp[j] + dp[j - 1]
                else:
                    dp[j] = 0

        return dp[n - 1]


solution = Solution()
grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(solution.uniquePathsWithObstacles(grid))  # Output: 2

solution = Solution()
grid = [[0, 0], [1, 1], [0, 0]]
result = solution.uniquePathsWithObstacles(grid)
print(result)  # Expected output: 0
