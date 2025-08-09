class Solution:
    """
    Function will get lexicographically sorted list of words : List[str]
    Returns the string of unique letters in alien language : str
    """
    def alienOrder(self, words: List[str]) -> str:
        # Adjacency list -> key = char : value = set of chars
        adj = {c: set() for word in words for c in word}
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        # Visited set to track already processed chars
        visited = set()
        # Visiting set to track, chars in current cycle
        visiting = set()
        # List of unique chars in alien order
        res = []

        # Postoder dfs which will return result in reverse order
        def dfs(char):
            if char in visiting:
                return False
            if char in visited:
                return True
            visiting.add(char)
            for nei in adj[char]:
                if not dfs(nei):
                    return False
            visiting.remove(char)
            visited.add(char)
            res.append(char)
            return True

        for char in adj:
            if not dfs(char):
                return ""
        res.reverse()
        return "".join(res)


