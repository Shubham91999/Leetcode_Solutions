from collections import defaultdict
from typing import List

class DetectSquares:
    def __init__(self):
        self.points = []
        self.pointMap = defaultdict(int)
    
    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.pointMap[tuple(point)] += 1  # point: count

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.points:
            if (abs(x-px) != abs(y-py)) or x==px or y==py:
                continue
            op1 = (x,py)
            op2 = (px,y)
            res += (self.pointMap[op1] * self.pointMap[op2])
        return res


    
