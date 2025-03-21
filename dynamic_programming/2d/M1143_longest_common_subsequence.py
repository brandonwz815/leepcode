# https://leetcode.com/problems/longest-common-subsequence/description/
# https://grok.com/chat/d4b717ba-58d8-416c-98af-258a9d3a4491

"""
Time: O(m*n)
Space: O(m*n)
"""


def longestCommonSubsequence(text1: str, text2: str) -> int:
    # Get lengths of both strings
    m, n = len(text1), len(text2)

    # Create a DP table with size (m+1) x (n+1)
    # Extra row and column for empty string cases
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If characters match, take diagonal value + 1
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            # If no match, take maximum of left or top value
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Return value at bottom-right corner
    return dp[m][n]


# Test cases
print(longestCommonSubsequence("abcde", "ace"))  # Output: 3
print(longestCommonSubsequence("abc", "abc"))  # Output: 3
print(longestCommonSubsequence("abc", "def"))  # Output: 0
