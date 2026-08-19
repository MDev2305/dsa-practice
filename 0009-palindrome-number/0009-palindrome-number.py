class Solution:
    def isPalindrome(self, x: int) -> bool:
        result=0
        num=x
        while x>0:
            last_digit=x%10
            result=(result*10) +last_digit
            x=x//10

        return result==num
            
