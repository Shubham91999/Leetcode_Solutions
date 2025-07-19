from typing import List
from math import isqrt

class Solution:
    def get_primes(self, n, m) -> List[int]:
        # Keeping True for 0, 1 and 2
        if n <= 2:
            return []
        is_prime = [True] * (n+1)
        is_prime[0], is_prime[1] = False, False

        for i in range(2, isqrt(n)+1):
            if is_prime[i]:
                for x in range(i*i, n+1, i):
                    is_prime[x] = False
        print(is_prime)
        return [i for i in range(n+1) if is_prime[i]][:m]

if __name__ == "__main__":
    s1 = Solution()
    primes = s1.get_primes(20, 3)
    print(primes)
