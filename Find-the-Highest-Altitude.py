class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = 0
        psum = 0
        for i in range(len(gain)):
            psum = psum + gain[i]
            result = max(result, psum)
        return result