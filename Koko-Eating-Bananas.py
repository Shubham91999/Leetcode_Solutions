class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1. Brute Force - count totaltime for speed starting from 1 to max(piles)
        # speed = 1
        # while True: 
        #     totalTime = 0 # Maintains total time taken in one iteration with speed n
        #     for pile in piles:
        #         totalTime += ceil(pile / speed) # Iterating over all the piles to calculate total time taken

        #     if totalTime <= h: # Total time should be less than or equal to given h
        #         return speed
        #     # if not, increment speed by and try with updated speed
        #     speed += 1
        # return speed 

        # 2. Binary Search
        l, r = 1, max(piles)  # Left -> 1 and right -> max of piles
        res = r   # currently res initilized to max of piles

        while l <= r:
            k = (l + r) // 2 # finding mid

            totalTime = 0 # calculating total time for current iteration with speed k
            for pile in piles:
                totalTime += math.ceil(pile / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res



            