class Solution:
    def sumZero(self, n: int) -> List[int]:
        middle = int(n/2)
        result = []
        if n%2 ==0:
            for i in range((-1)*middle,middle+1):
                if i != 0:
                    result.append(i)
        else:
            for i in range((-1)*middle,middle+1):
                result.append(i)
        return result