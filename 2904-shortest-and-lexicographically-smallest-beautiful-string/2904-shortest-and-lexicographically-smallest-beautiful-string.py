class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l = 0
        count = 0
        res = []
        resLen = float('inf')

        for r in range(len(s)):
            if s[r] == '1':
                count += 1

                while count == k:
                    curLen = r - l + 1

                    if curLen < resLen:
                        res = s[l:r + 1]
                        resLen = curLen
                    elif curLen == resLen:
                        res = min(res, s[l:r + 1])

                    if s[l] == '1':
                        count -= 1
                    l += 1
        # print(res)
        return res if resLen != float('inf') else ''
         # return s[start:end+1] if resLen != float('inf') else ''



                
