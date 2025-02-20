# https://leetcode.com/problems/climbing-stairs/
# https://gemini.google.com/app/4c8bfe08b2b4ca81

def climbStairs(n):
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
  
if __name__ == '__main__':
  print(climbStairs(3))