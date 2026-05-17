class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()
        queue = deque([start])

        while queue:
            i = queue.popleft()

            # Goal check
            if arr[i] == 0:
                return True

            # Mark visited to avoid cycles
            if i in visited:
                continue
            visited.add(i)

            # Explore both neighbors if within bounds
            for next_i in (i + arr[i], i - arr[i]):
                if 0 <= next_i < n and next_i not in visited:
                    queue.append(next_i)

        return False