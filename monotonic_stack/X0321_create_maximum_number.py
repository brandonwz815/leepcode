# https://leetcode.ca/all/321.html
# https://grok.com/chat/9ff9c508-840c-405d-8303-e7a53c67b3ca


def maxNumber(nums1, nums2, k):
    def get_max_subsequence(nums, length):
        stack = []
        drop = len(nums) - length  # Number of digits we can drop
        for num in nums:
            while stack and stack[-1] < num and drop > 0:
                stack.pop()
                drop -= 1
            stack.append(num)
        return stack[:length]  # Trim to desired length

    def merge(arr1, arr2):
        merged = []
        i, j = 0, 0
        while i < len(arr1) or j < len(arr2):
            # Compare remaining subsequences lexicographically
            if i < len(arr1) and (j >= len(arr2) or arr1[i:] > arr2[j:]):
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
        return merged

    m, n = len(nums1), len(nums2)
    max_result = [0] * k  # Initialize with smallest possible result

    # Try all possible combinations of digits from nums1 and nums2
    for i in range(max(0, k - n), min(k, m) + 1):
        if i <= m and k - i <= n:  # Ensure lengths are feasible
            sub1 = get_max_subsequence(nums1, i)
            sub2 = get_max_subsequence(nums2, k - i)
            candidate = merge(sub1, sub2)
            if candidate > max_result:  # Compare lexicographically
                max_result = candidate

    return max_result


# Example usage
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
print(maxNumber(nums1, nums2, k))  # Output: [9, 8, 6, 5, 3]
