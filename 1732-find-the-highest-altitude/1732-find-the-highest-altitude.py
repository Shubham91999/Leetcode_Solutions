class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        highest = 0
        for alt in gain:
            current += alt
            highest = max(highest, current)
        return highest