class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        # With double loop for angle wrap
        """
        # Get angle for point from current location
        def getAngle(p: List[int]) -> int:
            angle = math.atan2(p[0]-location[0], p[1]-location[1]) / (2*math.pi) * 360

            if angle < 0:
                angle += 360

            return angle

        angles = []
        same = 0

        for p in points:
            # point on top of location, increase same
            if p == location:
                same += 1
            else:
                angles.append(getAngle(p))

        # Sorting for sliding window application
        angles.sort()
        # Max points that can be seen
        ans = 0

        # Queue for sliding window
        queue = deque()

        for a in angles:
            # Added angle to sliding window queue
            queue.append(a)
            # Check if added angle in allowed angle frame -> a - queue[0] (starting of queue) 
            # if this subtraction exceeds allowed angle, then we need to pop from left (starting point)
            while a - queue[0] > angle:
                queue.popleft()

            ans = max(ans, len(queue))

        for a in angles:
            a += 360
            queue.append(a)
            # Check if added angle in allowed angle frame -> a - queue[0] (starting of queue) 
            # if this subtraction exceeds allowed angle, then we need to pop from left (starting point)
            while a - queue[0] > angle:
                queue.popleft()

            ans = max(ans, len(queue))
        return ans + same
        """

        # 2. Adding angles (+360) after sorting
        def getAngle(p: List[int]) -> int:
            angle = math.atan2(p[1]-location[1], p[0]-location[0]) / (math.pi*2) * 360 
            if angle < 0:
                angle += 360
            return angle

        angles = []
        same = 0
        # Populating angles array
        for p in points:
            if p == location:
                same += 1
            else:
                angles.append(getAngle(p))

        angles.sort()
        angles += [a + 360 for a in angles]

        # Looping through sorted angles, using sliding window to get max points
        ans = 0
        queue = deque()

        for a in angles:
            queue.append(a)

            while a - queue[0] > angle:
                queue.popleft()

            ans = max(ans, len(queue))

        return ans + same
        



            
 



        

