# https://leetcode.com/problems/maximum-subarray/description/
# https://gemini.google.com/app/1c98f519d88595aa


def maxSubArray(nums):
    max_so_far = nums[0]
    current_max = nums[0]

    for i in range(1, len(nums)):
        current_max = max(nums[i], nums[i] + current_max)
        max_so_far = max(max_so_far, current_max)

    return max_so_far


if __name__ == "__main__":
    print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
