from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # check if total cost == total gas
        if sum(cost) > sum(gas):
            return -1

        # solution is possible
        start = 0
        cur = 0

        for i in range(len(gas)):
            cur += gas[i] - cost[i]
            if cur < 0:
                cur = 0
                start = i + 1
        return start 