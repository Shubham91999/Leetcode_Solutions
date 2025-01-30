class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))
        print(num+1)
        num += 1
        result = [int(digit) for digit in str(num)]
        return result