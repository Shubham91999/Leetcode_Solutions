class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge Case
        if len(s1) > len(s2):
            return False

        # Count arrays to store count of chars in s1 and same window chars in s2
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # To maintain the count of matches
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:  # Traversing through both arrays to check matches
                matches += 1               # If match found, increment number

        # Sliding window part
        """
        We will check the number of matches with every possible window in s2.
        If number of matches reach 26, it means s1 matches with window from s2, return True
        """
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: 
                return True

            # Add character at r in window
            index = ord(s2[r]) - ord('a')   # Index of the char added to window
            s2Count[index] += 1             # Char added, so increasing the count

            """
            With changed count, there could be two possibilities:
            1) Count was different and now it matches in both count arrays
            2) Count was already matching, now it is different
            """
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # Remove character at l from window
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1

            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            l += 1  # Incrementing l to keep window size == len(s1)

        return matches == 26



            
        
