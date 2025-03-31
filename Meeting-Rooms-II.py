class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        min_heap = []  # Min-heap to track end times of meetings

        for interval in intervals:
            if min_heap and min_heap[0] <= interval[0]:  # Check if any room is free
                heapq.heappop(min_heap)  # Remove the room with the earliest end time

            heapq.heappush(min_heap, interval[1])  # Add the new meeting's end time

        return len(min_heap)