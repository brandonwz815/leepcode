# https://leetcode.com/problems/merge-intervals/description/


def merge(intervals):
    if not intervals:
        return []

    # Step 1: Sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        # If merged is empty or no overlap, add the new interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # Overlapping case: merge the intervals
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


if __name__ == "__main__":
    print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
