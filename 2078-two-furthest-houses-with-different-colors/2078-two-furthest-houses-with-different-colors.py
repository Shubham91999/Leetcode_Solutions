class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        # Brute Force
        """
        dist = 1

        for i in range(len(colors)):
            for j in range(len(colors)):
                if colors[i] != colors[j]:
                    dist = max(dist, abs(i-j))

        return dist
        """

        n = len(colors)
        dist = 0

        for i in range(n-1, -1, -1):
            if colors[i] != colors[0]:
                dist = max(dist, i)
                break

        for i in range(n):
            if colors[i] != colors[n-1]:
                dist = max(dist, n-1-i)
                break

        return dist
        