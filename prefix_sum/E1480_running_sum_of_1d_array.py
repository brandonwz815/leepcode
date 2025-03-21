# https://leetcode.com/problems/running-sum-of-1d-array/description/
# https://chatgpt.com/c/67b7340c-38bc-8001-a9d3-fe8aee3a8e7b


def runningSum(nums):
    # answer = []
    # current_sum = 0
    # for num in nums:
    #     current_sum += num
    #     answer.append(current_sum)
    # return answer

    n = len(nums)
    # ans = [nums[0]]
    ans = [nums[0]] * n
    for i in range(1, n):
        ans[i] = ans[i - 1] + nums[i]
        # ans.append(ans[i - 1] + nums[i])
    return ans


if __name__ == "__main__":
    print(runningSum([1, 2, 3, 4]))
