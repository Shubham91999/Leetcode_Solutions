"""
- Calculate degrees/angle for hr hand
    - Mod hr by 12 
    - hr * 30
    - Divide minutes by 12
    - minutes * 6
- Calculate degrees/angle for min hand
    - minutes * 6
- Abs diff of both
    - abs(mins-hr)
"""

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Calculating angle for hr hand
        hour_angle = (hour % 12) * 30 + (minutes / 12) * 6
        #print(hour_angle)

        # Calculating angle for min hand
        minute_angle = minutes * 6
        #print(minute_angle)

        res = abs(hour_angle-minute_angle)

        return min(res, 360-res)
        

        