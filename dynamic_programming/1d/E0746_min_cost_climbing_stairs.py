# https://leetcode.com/problems/min-cost-climbing-stairs/description/
# https://gemini.google.com/app/2f4cab891c07cf73


def min_cost_climbing_stairs(cost):
    """
    You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
    Once you pay the cost, you can either climb one or two steps. You can either start
    from the 0th index or the 1st index.

    Return the minimum cost to reach the top of the staircase.

    Args:
        cost: A list of integers representing the cost of each step.

    Returns:
        The minimum cost to reach the top of the staircase.
    """

    n = len(cost)

    # dp[i] stores the minimum cost to reach step i
    dp = [0] * (n + 1)  # Initialize dp array with size n+1

    # Base cases:
    dp[0] = 0  # Cost to reach the starting step (0th step) is 0
    dp[1] = 0  # Cost to reach the 1st step is also 0 (as you can start from there)

    # Iterate from the 2nd step to the top (n-th step):
    for i in range(2, n + 1):
        # The minimum cost to reach step i is the minimum of:
        # 1. Cost to reach step i-1 + cost to climb from i-1 to i
        # 2. Cost to reach step i-2 + cost to climb from i-2 to i
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

    return dp[n]  # The minimum cost to reach the top (n-th step)


# Example usage:
cost1 = [10, 15, 20]
print(min_cost_climbing_stairs(cost1))  # Output: 15

cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(min_cost_climbing_stairs(cost2))  # Output: 6

cost3 = [2, 5, 1, 7, 3, 9]
print(min_cost_climbing_stairs(cost3))  # Output: 13

# ------------------------------------------------------


# Optimized space solution (using only two variables):
def min_cost_climbing_stairs_optimized(cost):
    n = len(cost)
    if n <= 1:
        return 0

    prev1, prev2 = 0, 0  # Store costs for the previous two steps

    for i in range(2, n + 1):
        current = min(prev1 + cost[i - 1], prev2 + cost[i - 2])
        prev2 = prev1  # update previous 2
        prev1 = current  # update previous 1

    return prev1


cost1 = [10, 15, 20]
print(min_cost_climbing_stairs_optimized(cost1))  # Output: 15

cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(min_cost_climbing_stairs_optimized(cost2))  # Output: 6

cost3 = [2, 5, 1, 7, 3, 9]
print(min_cost_climbing_stairs_optimized(cost3))  # Output: 13
