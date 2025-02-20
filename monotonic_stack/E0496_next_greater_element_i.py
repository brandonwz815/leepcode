# https://leetcode.com/problems/next-greater-element-i
# https://chatgpt.com/c/67b69558-f088-8001-8ef5-077f8dbc21ed
# https://www.youtube.com/watch?v=68a1Dc_qVq4

from typing import List


def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    stack = []
    next_greater = {}

    # Traverse nums2 to find next greater elements
    for num in nums2:
        while stack and stack[-1] < num:
            smaller_num = stack.pop()
            next_greater[smaller_num] = num
        stack.append(num)

    # Assign -1 to remaining elements in the stack
    while stack:
        next_greater[stack.pop()] = -1

    # Map results for nums1
    return [next_greater[num] for num in nums1]


if __name__ == "__main__":
    print(nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
