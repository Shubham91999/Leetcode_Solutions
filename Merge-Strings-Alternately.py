class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # res = ""
        # #print(word2[2:len(word2)+1])
        # len1 = len(word1)
        # len2 = len(word2)
        # n = min(len1, len2)

        # for i in range(n):
        #     res += word1[i] + word2[i]
        # if len1 == len2:
        #     return res
        # if len1 > len2:
        #     res+=word1[i+1:]
        # if len1 < len2:
        #     res+=word2[i+1:]
        # return res

        # Optimized with List 
        res = [] # List to store each character from two strs
        len1 = len(word1)
        len2 = len(word2)
        n = min(len1, len2)

        for i in range(n):
            res.append(word1[i])
            res.append(word2[i])
        res.append(word1[n:])
        res.append(word2[n:])
        return "".join(res)



        

            

