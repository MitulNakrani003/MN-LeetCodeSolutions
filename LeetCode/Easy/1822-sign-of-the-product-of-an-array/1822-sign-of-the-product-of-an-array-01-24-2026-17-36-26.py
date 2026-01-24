class Solution:
    def arraySign(self, nums: List[int]) -> int:
        result = 1
        for x in nums:
            if x < 0:
                result*=(-1)
            elif x > 0:
                result*=1
            else:
                return 0
        return result