class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # Brute Force -> Time: O(n^2) Space: O(n)
        """
        res = 0
        colorlist = list(colors)
        removed = True
        

        while removed:
            removed = False
            for i in range(1, len(colorlist)):
                if i < len(colorlist) and colorlist[i-1] == colorlist[i]:
                    if neededTime[i-1] <= neededTime[i]:
                        res += neededTime[i-1]
                        colorlist.pop(i-1)
                        neededTime.pop(i-1)
                        removed = True
                    elif neededTime[i-1] > neededTime[i]:
                        res += neededTime[i]
                        colorlist.pop(i)
                        neededTime.pop(i)
                        removed = True
                    
        return res
        """

        # Initalize two pointers i, j.
        total_time = 0
        i, j = 0, 0
        
        while i < len(neededTime) and j < len(neededTime):
            curr_total = 0
            curr_max = 0
            
            # Find all the balloons having the same color as the 
            # balloon indexed at i, record the total removal time 
            # and the maximum removal time.
            while j < len(neededTime) and colors[i] == colors[j]:
                curr_total += neededTime[j]
                curr_max = max(curr_max, neededTime[j])
                j += 1
            
            # Once we reach the end of the current group, add the cost of 
            # this group to total_time, and reset two pointers.
            total_time += curr_total - curr_max
            i = j
        
        return total_time