# https://leetcode.ca/all/253.html
# https://chatgpt.com/c/67b5131a-1abc-8001-bc77-46e3d35cba3f
# https://www.youtube.com/watch?v=FdzJmTCVyJU

import heapq

def minMeetingRooms(intervals):
    if not intervals:
        return 0

    # Step 1: Sort meetings by start time
    intervals.sort(key=lambda x: x[0])

    # Min-heap to track the end times of meetings
    heap = []

    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heappop(heap)  # Free up a room (remove the earliest ending meeting)
        
        heapq.heappush(heap, end)  # Allocate a new room

    return len(heap)  # Number of rooms needed

# Example Usage:
intervals = [[0, 30], [5, 10], [15, 20]]
print(minMeetingRooms(intervals))  # Output: 2

