# https://leetcode.com/problems/non-overlapping-intervals/description/
# https://chatgpt.com/c/67b68fcc-6c9c-8001-ba59-4c0917e7f6a7


def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0

    # Step 1: Sort by end times
    intervals.sort(key=lambda x: x[1])

    count = 0  # Number of intervals to remove
    prev_end = float("-inf")  # Track the end of the last non-overlapping interval

    for start, end in intervals:
        if start >= prev_end:
            # No overlap, update last included interval's end time
            prev_end = end
        else:
            # Overlap, remove this interval (increment count)
            count += 1

    return count


if __name__ == "__main__":
    print(eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
    print(eraseOverlapIntervals([[1, 2], [2, 3]]))
