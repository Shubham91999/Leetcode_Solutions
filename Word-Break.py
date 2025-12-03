from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 1. Brute Force - O(m*l*2^n)
        # Helper function to check if we can segment the string from the current index 'start'
        # def canSegment(start):
        #     # If we have reached the end of the string, it means the string can be segmented successfully
        #     if start == len(s):
        #         return True
            
        #     # Try every word in the dictionary
        #     for word in wordDict:
        #         # Check if the substring starting at 'start' and of length 'word' matches the current word
        #         if s[start:start + len(word)] == word:
        #             # If it matches, recursively check if the remaining substring can also be segmented
        #             if canSegment(start + len(word)):
        #                 return True
            
        #     # If no word matches, return False (meaning no segmentation found for this part)
        #     return False
    
        # # Start checking the string from index 0
        # return canSegment(0)

        # 2. Brute Force Recursion:
        # def dfs(i):
        #     if i == len(s):
        #         return True

        #     for w in wordDict:
        #         if ((i+len(w)) <= len(s) and s[i:i+len(w)] == w):
        #             if dfs(i+len(w)):
        #                 return True
        #     return False
        # return dfs(0)

        # 3. Dynamic Programming Top-Down
        # memo = {len(s):True}
        # def dfs(i):
        #     if i in memo:
        #         return memo[i]

        #     for w in wordDict:
        #         if (i+len(w) <= len(s) and s[i:i+len(w)] == w):
        #             if dfs(i+len(w)):
        #                 memo[i] = True
        #                 return True
        #     memo[i] = False
        #     return False
        # return dfs(0)

        # 4. Bottom up approach
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i:i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                    if dp[i]:
                        break

        return dp[0]




        