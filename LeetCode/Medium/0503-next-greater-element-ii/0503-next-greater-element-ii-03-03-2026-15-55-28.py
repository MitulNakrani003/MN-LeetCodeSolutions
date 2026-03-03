class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        monotonicstack = []
        resultarr  = [0] * len(nums)
        for i in range(2*len(nums)-1, -1, -1):
            index = i % len(nums)
            # print(i, index)
            while monotonicstack and monotonicstack[-1] <= nums[index]:
                monotonicstack.pop()
            if i < len(nums):
                resultarr[i] = monotonicstack[-1] if monotonicstack else -1
            # print(resultarr)
            monotonicstack.append(nums[index])
            # print(monotonicstack)
        # print(resultarr)
        return resultarr