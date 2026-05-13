class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        # Create a boolean array of size n
        prime = [True] * n
        prime[0] = prime[1] = False

        for p in range(2, int(n ** 0.5) + 1):
            if prime[p]:
                for i in range(p * p, n, p):
                    prime[i] = False

        return sum(prime)

