class Solution:
    def countCollisions(self, directions: str) -> int:
        # Brute Force -> O(n^2)
        """
        dirs = list(directions)
        collisions = 0

        flag = True

        while flag:
            flag = False
            new_dir = dirs.copy()

            i = 0
            while i < len(dirs) - 1:
                pair = dirs[i] + dirs[i+1] 

                if pair == 'RL':
                    collisions += 2
                    new_dir[i] = new_dir[i+1] = 'S'
                    flag = True
                    i += 2

                if pair == 'RS':
                    collisions += 1
                    new_dir[i] = new_dir[i+1] = 'S'
                    flag = True
                    i += 2

                if pair == 'SL':
                    collisions += 1
                    new_dir[i] = new_dir[i+1] = 'S'
                    flag = True
                    i += 2
                else:
                    i += 1

            dirs = new_dir

        return collisions
        """

        # Optimal -> O(n)

        collisions = 0
        n = len(directions)
    
        # Trim leading L
        i = 0
        while i < n and directions[i] == 'L':
            i += 1
        # Trim trailing R
        j = n - 1
        while j >= 0 and directions[j] == 'R':
            j -= 1
        # Count number of R and L in reamining string
        middle = directions[i:j+1]

        for c in middle:
            if c == 'R' or c == 'L':
                collisions += 1
            
        return collisions




        