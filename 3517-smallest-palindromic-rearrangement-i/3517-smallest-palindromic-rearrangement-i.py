class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)
        middle = ""
        left_half = []
    
        for ch in sorted(freq.keys()):
            count = freq[ch]
            if count % 2 == 1:
                if not middle:
                    middle = ch
                else:
                    # Guaranteed input is a palindrome, so won't hit this
                    pass
            left_half.append(ch * (count // 2))
        
        left = ''.join(left_half)
        return left + middle + left[::-1]