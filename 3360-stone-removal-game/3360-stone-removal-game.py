"""
- Alice goes first
- Alice first turn -> removes 10 stones
- Next turns, 1 fewer stone from number of last removed stones
- Player who cannot make a move loses the game
- True if Alice wins, false otherwise

- if starting n less than 10 -> Bob wins -> return False
- 19 -> 10, 9, no stones for Alice -> False 
- 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0
-  A, B, A, B, A, B, A, B, A, B, A

- if current removed number - 1 is present -> game continues
- if not, 
"""

class Solution:
    def canAliceWin(self, n: int) -> bool:
        # simulation
        # start with take = 10
        # moves made k = 0
        # game will continue till number of remaining stones satisfy the take requirement 
        take = 10
        k = 0
        while n >= take:
            n -= take
            take -= 1
            k += 1
        # Alice moves first, so she makes the odd-numbered moves 
        # Bob makes the even-numbered moves 
        # Player with last move, wins the game
        # Alice wins if k is odd, Bob wins if k is even
        return k % 2 == 1 # returns true if k is odd (Alice wins)