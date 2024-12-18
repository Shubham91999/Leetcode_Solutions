class Solution(object):
    def groupAnagrams(self, strs):
        
        """
        1. Sorting string and grouping together
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return res.values()"""

        #. Hashtable with elphabet count as key
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())