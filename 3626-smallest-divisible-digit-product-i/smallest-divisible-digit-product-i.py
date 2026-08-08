class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        a = n

        while True:
            temp = a
            product = 1

            while temp > 0:
                digit = temp % 10
                product *= digit
                temp //= 10

            if product % t == 0:
                return a

            a += 1
        