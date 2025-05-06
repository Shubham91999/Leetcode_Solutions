class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        for target in [tops[0], bottoms[0]]: # This will iterate over both faces of first domino, we are considering only first coz if any of the face is not matching with remining, it break our condition of having atleast one face common in all pairs(top, bottom)
            missingT, missingB = 0, 0 # To count mising occurences 
            for i, pair in enumerate(zip(tops, bottoms)):  # index, (top, bottom)
                top, bottom = pair
                if not (top == target or bottom == target): # if any of the top or bottom is not equal to target (top[0] or bottom[0] in next iteration)
                    break
                if top != target:  # Target is missing in top array, increment the count
                    missingT += 1
                if bottom != target:  # Target is missing in bottom array, increment the count
                    missingB += 1
                if i == len(tops)-1:  # i reached end, it means we found target which appears atleast once in top or bottom array, we also have missing count
                    return min(missingT, missingB)  # Returning min
                
        return -1


