"""
Intuition
There should be some kind of formula here...

Approach
Let:

ls and rs be sums of numeric elements of the left and right half of num
lm and rm be counts of ? in the left and right half of num
lam and ram be number of Alice's moves in the left and right half
lbm and rbm be number of Bob's moves in the left and right half
Then Alice wins if, and only if:
ls + 9*lam > rs + 9*rbm
OR
rs + 9*ram > ls + 9*lbm
because on each move Alice tries to increase the imbalance between the right and left halves of num and Bob tries to reduce it.

Taking into consideration that lbm === lm - lam and rbm === rm - ram, we can rewrite the above inequalities:
ls + 9*lam > rs + 9*(rm - ram) => ls + 9*(lam+ram) > rs + 9*rm
rs + 9*ram > ls + 9*(lm - lam) => rs + 9*(lam+ram) > ls + 9*lm

Now, note that (lam+ram) is the total number of possible Alice's moves, which equals to (lm+rm+1)//2, taking into account that Alice moves first and has one move more than Bob if total number of moves is odd.

Thus, the task comes down to calculating the sums of the digits and counts of ? in the right and left halves of the num, which could be done in one pass.
"""

class Solution:
    def sumGame(self, num: str) -> bool:
        mid = len(num) // 2

        ls, lm = self.getStates(num[:mid]) # Digit sum of left half, Number of ? in left half
        rs, rm = self.getStates(num[mid:]) # Digit sum of right half, Number of ? in right half

        # Alice's moves
        alice_moves = (lm + rm + 1)//2

        # left is greater
        left_wins = ls + 9*alice_moves > rs + 9*rm

        # Right is greater 
        right_wins = rs + 9*alice_moves > ls + 9*lm

        return left_wins or right_wins # Returns True if any of them is 1/True

    def getStates(self, num: str) -> List[int]:
        digit_sum = 0
        counter = 0

        for c in num:
            if c == '?':
                counter += 1
            else:
                digit_sum += int(c)

        return [digit_sum, counter]

    
        