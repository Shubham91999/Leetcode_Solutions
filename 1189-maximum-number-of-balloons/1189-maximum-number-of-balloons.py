class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        refMap = defaultdict(int)
        for c in 'balloon':
            refMap[c] += 1

        textMap = defaultdict(int)
        for c in text:
            textMap[c] += 1

        # first check if all key - value pairs satisfy condition in refMap
        result = float('inf')
        for key, value in refMap.items():
            if key not in textMap or value == 0:
                return 0
            result = min(result, textMap[key] // value)
        return result