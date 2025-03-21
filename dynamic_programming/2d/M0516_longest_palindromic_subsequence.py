# https://leetcode.com/problems/longest-palindromic-subsequence/description/
# https://grok.com/chat/84688180-adad-44f9-abf9-310b219d01b5


def longestPalindromeSubseq(s: str) -> int:
    n = len(s)
    # Create a 2D DP table initialized with 0s
    dp = [[0] * n for _ in range(n)]

    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    # Fill the dp table
    # cl is the chain length (length of substring we're considering)
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1  # ending index of current substring

            # If first and last characters match
            if s[i] == s[j] and cl == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                # Take maximum of substring excluding either end
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # Return the value for the entire string
    return dp[0][n - 1]


# Example usage:
print(longestPalindromeSubseq("bbbab"))  # Output: 4 ("bbbb")
print(longestPalindromeSubseq("cbbd"))  # Output: 2 ("bb")
