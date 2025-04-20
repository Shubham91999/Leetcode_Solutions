class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. Brute Force: Sorted string key in hashmap
        # res = defaultdict(list)
        # for s in strs:
        #     sortedS = ''.join(sorted(s)) # Sorting every string in strs
        #     res[sortedS].append(s) # Using sorted string as key in hashmap
        # return list(res.values())

        # Hashtable with count array
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26 # Count array to store count of a .... z

            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

