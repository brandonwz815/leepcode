# https://leetcode.com/problems/product-of-array-except-self/description/
# https://grok.com/chat/b54b21c6-ee99-4108-9463-fc9825ed2446
# https://www.youtube.com/watch?v=bNvIQI2wAjk


""" def productExceptSelf(nums):

    n = len(nums)
    leftPass = [1] * n
    leftPass[0] = nums[0]
    for i in range(1, n - 1):
        leftPass[i] = leftPass[i - 1] * nums[i]
    print(leftPass)

    rightPass = [1] * n
    for i in range(n - 2, -1, -1):
        rightPass[i] = rightPass[i + 1] * nums[i + 1]
    print(rightPass)

    ans = [0] * n
    for i in range(n):
        ans[i] = rightPass[i] * leftPass[i]
    return ans """

def productExceptSelf(nums):
    n = len(nums)
    leftPass = [1] * n
    for i in range(1, n):
        leftPass[i] = leftPass[i - 1] * nums[i - 1]  # Elements before i
    print(leftPass)
    
    rightPass = [1] * n
    for i in range(n - 2, -1, -1):
        rightPass[i] = rightPass[i + 1] * nums[i + 1]  # Elements after i
    print(rightPass)
    
    ans = [0] * n
    for i in range(n):
        ans[i] = leftPass[i] * rightPass[i]
    return ans


""" def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n  # Initialize output array with 1s

    # First pass: Compute prefix products
    # answer[i] will hold product of all elements to the left of i
    for i in range(1, n):
        answer[i] = answer[i - 1] * nums[i - 1]

    # Second pass: Multiply by suffix products
    # Use a running product from the right
    right_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] = answer[i] * right_product
        right_product *= nums[i]

    return answer """


if __name__ == "__main__":
    print(productExceptSelf([1, 2, 3, 4]))
