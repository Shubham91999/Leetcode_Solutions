class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        cache = {}

        def getTotal(stoneValue, i) -> int:
            # Cache check
            if i in cache:
                return cache[i]

            # Base case: all stones have been taken
            if i >= len(stoneValue):
                return 0

            # Recursive cases: Three choices
            first = stoneValue[i] - getTotal(stoneValue, i+1)
            best = first
            
            if i + 1 < len(stoneValue):
                second = stoneValue[i] + stoneValue[i+1] - getTotal(stoneValue, i+2)
                best = max(best, second)
            
            if i + 2 < len(stoneValue):
                third = stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - getTotal(stoneValue, i+3)
                best = max(best, third)

            cache[i] = best
            return best

        total = getTotal(stoneValue, 0)

        if total > 0:
            return "Alice"
        elif total < 0:
            return "Bob"
        else:
            return "Tie"



        