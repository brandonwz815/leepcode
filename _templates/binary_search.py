# https://grok.com/chat/1840bca6-78bf-466b-91a2-d826ba6d205b


def binary_search_bad(arr, target):
    left = 0
    right = len(arr) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid
        else:
            right = mid
    return -1  # No final checks!
