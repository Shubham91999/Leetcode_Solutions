class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 1. Reverse and Transpose 
        # Reverse
        # matrix.reverse()

        # # Transpose
        # for i in range(len(matrix)):
        #     for j in range(i+1, len(matrix)):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Rotating by four calls
        left, right = 0, len(matrix)-1

        while left < right:
            for i in range(right-left):
                top, bottom = left, right

                # Storing top left
                topLeft = matrix[top][left+i]
                # Bottom left to top left
                matrix[top][left+i] = matrix[bottom-i][left]
                # Bottom right to bottom left
                matrix[bottom-i][left] = matrix[bottom][right-i]
                # Top right to bottom right
                matrix[bottom][right-i] = matrix[top+i][right]
                # Top left to top right
                matrix[top+i][right] = topLeft

            # Updating pointers
            left += 1
            right -= 1

