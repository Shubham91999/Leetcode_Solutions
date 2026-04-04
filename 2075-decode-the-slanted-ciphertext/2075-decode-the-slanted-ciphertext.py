class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        # Edge case: empty string
        if not encodedText:
            return ""
        
        # Total columns in the matrix
        cols = len(encodedText) // rows
        
        result = []
        
        # Start from each column in the first row
        for start_col in range(cols):
            r = 0
            c = start_col
            
            # Move diagonally down-right
            while r < rows and c < cols:
                result.append(encodedText[r * cols + c])
                r += 1
                c += 1
        
        # Remove trailing spaces and return
        return "".join(result).rstrip()