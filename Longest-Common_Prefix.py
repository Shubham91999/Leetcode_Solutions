class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 1. Vertical Scanning
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

        # 2. Horizontal Scanning
        # prefix = strs[0]
        # for i in range(1, len(strs)):
        #     j = 0
        #     while j < min(len(prefix), len(strs[i])):
        #         if prefix[j] != strs[i][j]:
        #             break
        #         j += 1
        #     prefix = prefix[:j]
        # return prefix

