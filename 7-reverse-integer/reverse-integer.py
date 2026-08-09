class Solution:
    def reverse(self, x: int) -> int:
        a=abs(x)
        rev=0
        while a>0:
            digit=a%10
            rev=rev*10+digit
            a=a//10
        if x<0:
            rev=-rev
        if -2**31<=rev<=2**31-1:
            return rev
        else:
            return 0