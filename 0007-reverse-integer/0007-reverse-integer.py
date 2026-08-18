class Solution:
    def reverse(self, x: int) -> int:
        result = 0

        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1

        while x > 0:
            last_digit = x % 10
            result = result * 10 + last_digit
            x = x // 10

        result = result * sign

        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result
        