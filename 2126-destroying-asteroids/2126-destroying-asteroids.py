"""
plant = 5
asteroids = [4, 4, 9, 23]

total = 5, asteroid = 4
total > asteroid -> total = 5 + 4 = 9

total = 9, asteroid = 4
X total > asteroid -> total = 9 + 4 = 13
 


"""

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids = sorted(asteroids)
        total = mass

        for ast in asteroids:
            if total < ast:
                return False
            total = total + ast

        return True