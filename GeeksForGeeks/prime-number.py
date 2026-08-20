# Question: Given a number n, determine whether it is a prime number or not.
# A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

class Solution:
    def isPrime(self, n):
        if n <= 1:
            return False

        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False

        return True
