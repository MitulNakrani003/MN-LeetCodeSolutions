class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        result = [0] * (m+n)
        
        for i in range(m-1,-1,-1):
            carry = 0
            for j in range(n-1,-1,-1):
                mul = int(num1[i]) * int(num2[j]) + carry
                sum_ = mul + result[i + j + 1]
                result[i + j + 1] = sum_ % 10
                result[i + j] += sum_ // 10


        product = ''.join(map(str, result)).lstrip('0')
        return product if product else "0"

