class Solution:
    def myPow(self, x: float, n: int) -> float:
        def positivePow(x,n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            res = positivePow(x, n // 2)
            res = res * res

            if n % 2 == 1:
                return res * x
            
            return res
            
        if n >= 0:
            return positivePow(x,n)
        else:
            return 1/positivePow(x,abs(n))