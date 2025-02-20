# https://leetcode.com/problems/insert-interval/description/
# https://chatgpt.com/c/67b689ee-9d4c-8001-bc05-8c8e31145c7f


def insert(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)

    # Add all intervals ending before newInterval starts
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Merge overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    result.append(newInterval)

    # Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result


if __name__ == "__main__":
    print(insert([[1, 3], [6, 9]], [2, 5]))
