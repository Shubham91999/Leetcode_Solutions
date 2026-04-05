class Solution:
    def judgeCircle(self, moves: str) -> bool:
        vertical_count = 0
        horizontal_count = 0

        for move in moves:
            if move == 'U':
                vertical_count += 1
            elif move == 'D':
                vertical_count -= 1
            elif move == 'L':
                horizontal_count -= 1
            elif move == 'R':
                horizontal_count += 1
            else:
                print("Invalid move")

        if vertical_count == 0 and horizontal_count == 0:
            return True
        return False  