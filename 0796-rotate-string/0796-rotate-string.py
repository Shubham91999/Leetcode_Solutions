class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        double_string = s + s 

        return double_string.find(goal) != -1