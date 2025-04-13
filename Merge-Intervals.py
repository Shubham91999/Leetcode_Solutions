class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. Sorting
        # intervals.sort(key = lambda i: i[0])  # Sorting pairs of intervals based on start time
        # output = [intervals[0]]     # Assigning first interval to output, handling edge cases

        # for start, end in intervals[1:]:  # For every start and end in intervals list from 1st position
        #     lastEnd = output[-1][1]  # Endtime of last element in output

        #     if start <= lastEnd:  # If start of current is less that last end i.e. overlapping intervals
        #         output[-1][1] = max(lastEnd, end)  # [[1, 5], [2, 4]] -> [1, 5]
        #     else:
        #         output.append([start, end])  # Non-overlapping intervals # [[1, 5], [8, 10]] -> [[1, 5], [8, 10]]
        # return output

        # 2. Greedy Approach
        max_val = max(interval[0] for interval in intervals)
        
        mp = [0] * (max_val + 1)
        for start, end in intervals:
            mp[start] = max(end + 1, mp[start])

        res = []
        have = -1
        interval_start = -1
        for i in range(len(mp)):
            if mp[i] != 0:
                if interval_start == -1:
                    interval_start = i
                have = max(mp[i] - 1, have)
            if have == i:
                res.append([interval_start, have])
                have = -1
                interval_start = -1

        if interval_start != -1:
            res.append([interval_start, have])

        return res
