class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone = set()
        for char in jewels:
            stone.add(char)
        count = 0
        for char in stones:
            if char in stone:
                count += 1
                #print(char, count)

        #print(stone)
        return count