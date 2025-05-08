class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # # Visit sr,sc
        # # BFS on its adjancent (vertically, horizontally)
        # # Check if they are to be colored (1)
        # # if yes, color and bfs on adjacent

        # # Getting color of starting point
        # cur_color = image[sr][sc]
        # if color == cur_color:
        #     return image
        # ROWS, COLS = len(image), len(image[0])

        # # Function to paint the pixel
        # def dfs(cr, cc):  # Updated current row, current 
        #     # cr and cc should be inbounds, current pixel should have color same as starting point, it shouldnt be already visited
        #     if cr in range(ROWS) and cc in range(COLS) and image[cr][cc] == cur_color:
        #         image[cr][cc] = color # All conditions staisfied, so changing color
        #         dfs(cr+1, cc) # Calling dfs on neighbors (vertical and horizontal)
        #         dfs(cr-1, cc)
        #         dfs(cr, cc+1)
        #         dfs(cr, cc-1)

        # dfs(sr, sc)
        # return image
        directions = [(1,0), (-1,0), (0,1), (0,-1)]    

        queue = deque([(sr, sc)])  # Queue for BFS
        visited = set([sr, sc])  # Set to maitain visited pixels
        original_color = image[sr][sc] # Getting original color
        ROWS, COLS = len(image), len(image[0])

        while len(queue) > 0:
            r, c = queue.popleft()  

            if image[r][c] == original_color:  # If current pixel color matches original, paint with new color
                image[r][c] = color
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc # for neighbors

                    if (nr not in range(ROWS) or nc not in range(COLS) or (nr, nc) in visited):
                        continue

                    # Adding in queue for further processing
                    queue.append((nr,nc))
                    # Adding in set to avoid visiting again
                    visited.add((nr,nc))
        return image


        



       
        
        
