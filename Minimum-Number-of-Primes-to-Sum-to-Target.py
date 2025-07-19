# 1. Find prime numbers till n
# 2. Consider only first m prime numbers
# 3. Out of selected prime numbers, find out the pairs that sum up to n
# 4. Compare length of those pairs and return the smallest one

class Solution:
    # 1. Brute Force to find primes till n
    # def is_prime(self, n) -> bool:
    #     if n == 3 or n == 3:
    #         return True
    #     for i in range(2, n):
    #         if n % i == 0:
    #             return False
    #     return True

    # def get_primes(self, n, m):
    #     primes = []
    #     for i in range(2, n + 1):
    #         if self.is_prime(i):
    #             primes.append(i)
    #             if len(primes) == m:
    #                 break
    #     return primes

    # def minNumberOfPrimes(self, n: int, m: int) -> int:
    #     primes = self.get_primes(n, m)
    #     cache = {}
    #     def dp(curr_sum):
    #         if curr_sum == n:
    #             return 0
    #         if curr_sum > n:
    #             return float('inf')
    #         if curr_sum in cache:
    #             return cache[curr_sum] 

    #         min_count = float('inf')
    #         for prime in primes:
    #             min_count = min(min_count, dp(curr_sum + prime) + 1)
    #         cache[curr_sum] = min_count
    #         return min_count

    #     res = dp(0)
    #     return res if res != float('inf') else -1

# 2. Optimized with Sieve of Eratosthenes for getting primes + dp
    def get_primes(self, n, m) -> List[int]:
        # Keeping True for 0, 1 and 2
        if n < 2:
            return []
        is_prime = [True] * (n+1)
        is_prime[0], is_prime[1] = False, False

        for i in range(2, isqrt(n)+1):
            if is_prime[i]:
                for x in range(i*i, n+1, i):
                    is_prime[x] = False
        return [i for i in range(n+1) if is_prime[i]][:m]


    def minNumberOfPrimes(self, n: int, m: int) -> int:
        primes = self.get_primes(n, m)
        cache = {}

        def dp(curSum: int):
            if curSum == n:
                return 0
            if curSum > n:
                return float('inf')
            if curSum in cache:
                return cache[curSum]

            min_count = float('inf')
            for prime in primes:
                min_count = min(min_count, dp(curSum + prime) + 1)
            cache[curSum] = min_count
            return min_count
        res = dp(0)
        return res if res != float('inf') else -1




    
    

