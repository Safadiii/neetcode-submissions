class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if x == 0:
            return 0.0

        final_result = 1.0

        if n < 0:
            x = 1/x
            n = -n
        while n > 0:
            if n%2 == 1:
                final_result *= x
            x *= x
            n //= 2
        return final_result



        