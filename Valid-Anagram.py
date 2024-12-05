class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        #Approach 1 = Sorting both the strings and then comparing the sorted strings

        # sorted_s = ''.join(sorted(s))
        # sorted_t = ''.join(sorted(t))
        # print(sorted_s)
        # print(sorted_t)
        # if sorted_s == sorted_t:
        #     return True
        # else:
        #     return False

        # sorted_s = sorted(s)
        # sorted_t = sorted(t)
        # if sorted_s == sorted_t:
        #     return True
        # else: 
        #     return False

        #Approach 2 = Using counter 
        return Counter(s) == Counter(t)


