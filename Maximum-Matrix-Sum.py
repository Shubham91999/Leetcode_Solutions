from typing import List
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # we will track total sum, number of negatives and minimum number till now, with every matrix element
        total_sum = negs = 0
        cur_min = float('inf')

        rows, cols = len(matrix), len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                total_sum += abs(matrix[r][c])
                if matrix[r][c] < 0:
                    negs += 1
                cur_min = min(cur_min, abs(matrix[r][c]))

        # calculating final result
        # if count of negative numbers is odd, subtract 2 * cur_min from total sum
        res = total_sum
        if negs % 2:
            res = total_sum - (2 * cur_min)

        return res

        
