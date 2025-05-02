class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words) # To avoid checking same word multiple times
        dp = {}

        def dfs(word):
            if word in dp:
                return dp[word]

            for i in range(1, len(word)): # Starting prefix from index 1, as with empty prefix we will have same word as suffix and it will return true
                prefix = word[:i]  # Prefix -> starting from 1 to i (exclusive)
                suffix = word[i:]  # suffix -> starting from i to end of string

                # prefix in wordSet and suffix in wordSet -> if both found in wordSet
                # prefix in wordSet and dfs(suffix) -> prefix found, suffix is broken into more words
                if ((prefix in wordSet and suffix in wordSet) or (prefix in wordSet and dfs(suffix))):
                    dp[word] = True
                    return dp[word]
            dp[word] = False
            return dp[word]

        res = [] # List of concatenated words
        for w in words: # Calling dfs for each word in list
            if dfs(w): # If dfs returns true, it means it is a concatenated word, append it in result list
                res.append(w)
        return res