class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for n in range(numRows):
            row = [1]
            val = 1
            for k in range(1, n+1):
                val = val * (n-k+1) // k
                row.append(val)
            res.append(row)
        return res