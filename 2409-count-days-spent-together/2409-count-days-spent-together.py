"""
- Convert the arrive and leave dates -> day of the year

- Max of the arrival date -> later arrival date -> max(arriveAliceDay, arriveBobDay)
- Min of the departure data -> earlier departure date -> min(leaveAliceDay, leaveBobDay)

- If earlier departure date is on or after the later arrival date:
    - min(leaveAliceDay, leaveBobDay) - max(arriveAliceDay, arriveBobDay) + 1 (dates inclusive)

- max(0, min(leaveAliceDay, leaveBobDay) - max(arriveAliceDay, arriveBobDay) + 1)
"""

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        datesOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        prefixSum = [0]
        for date in datesOfMonth:
            prefixSum.append(prefixSum[-1] + date)
        # print(prefixSum) -> [0, 31, 59, 90, 120, 151, 181, 212, 242, 273, 303, 334]

        # helper to count the day
        def calculateDay(day: str) -> int:
            month = int(day[:2]) # first two chars of the string
            date = int(day[3:]) # chars from third index to last

            return prefixSum[month-1] + date

        # Getting days count for all four input dates
        arriveAliceDay = calculateDay(arriveAlice)
        arriveBobDay = calculateDay(arriveBob)
        leaveAliceDay = calculateDay(leaveAlice)
        leaveBobDay = calculateDay(leaveBob)

        laterArrival = max(arriveAliceDay, arriveBobDay)
        earliestDeparture = min(leaveAliceDay, leaveBobDay)

        return max(0, earliestDeparture - laterArrival + 1)

        
        