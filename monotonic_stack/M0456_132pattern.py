# Wrong solution from meta.ai
# def find132pattern(nums):
#     stack = []
#     s3 = float('inf')

#     for n in nums:
#         print(stack)
#         if n < s3:
#             return True
#         while stack and stack[-1] < n:
#             s3 = stack.pop()
#         stack.append(n)

#     return False

# ---------------------------------------------------------

# chatgpt, difficult to explain
# def find132pattern(nums):
#     n = len(nums)
#     if n < 3:
#         return False

#     stack = []  # This will store potential nums[k] values
#     third = float('-inf')  # This is nums[k], initially set to negative infinity

#     # Traverse the array in reverse
#     for i in range(n - 1, -1, -1):
#         # Check if we found a valid nums[i] < nums[k]
#         if nums[i] < third:
#             return True
#         # Update the stack and third
#         while stack and nums[i] > stack[-1]:
#             third = stack.pop()
#         # Add the current number as a potential nums[j]
#         stack.append(nums[i])
#         print(stack)
#     return False

# ---------------------------------------------------------


# https://www.youtube.com/watch?v=q5ANAl8Z458
def find132pattern(nums):
    stack = []
    curMin = nums[0]

    for k in nums[1:]:
        while stack and stack[-1][0] <= k:
            stack.pop()
        if stack and stack[-1][0] > k:
            return True
        stack.append([k, curMin])
        curMin = min(curMin, k)
    return False


print(find132pattern([3, 0, 4, 5, 3]))
print(find132pattern([1, 2, 3, 4]))
