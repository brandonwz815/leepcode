# https://leetcode.com/problems/next-greater-element-ii/description/
# https://grok.com/chat/7c562a43-a51e-4363-9006-2a087235d1c4


def nextGreaterElements(nums):
    n = len(nums)
    result = [-1] * n  # Initialize result array with -1
    stack = []  # Monotonic stack to store indices

    # Iterate twice since it's circular
    for i in range(2 * n):
        curr = nums[i % n]  # Get current element using modulo for circular property

        # Pop elements from stack while current element is greater
        while stack and nums[stack[-1]] < curr:
            result[stack.pop()] = curr

        if i < n:
            stack.append(i)  # Only push indices in first iteration

    return result


if __name__ == "__main__":
    print(nextGreaterElements([1, 2, 1]))
    print(nextGreaterElements([1, 2, 3, 4, 3]))

# Example usage:
# nums = [1,2,1]
# Output: [2,-1,2]
# nums = [1,2,3,4,3]
# Output: [2,3,4,-1,4]
