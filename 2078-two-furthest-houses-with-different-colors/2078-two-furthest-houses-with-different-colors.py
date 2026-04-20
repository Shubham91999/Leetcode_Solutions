class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        dist = 1

        for i in range(len(colors)):
            for j in range(len(colors)):
                if colors[i] != colors[j]:
                    dist = max(dist, abs(i-j))

        return dist
        