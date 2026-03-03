class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        monotonicstack = []
        resultarr  = []
        resultmap = {}
        for i in range(len(nums2)-1, -1, -1):
            if len(monotonicstack) == 0:
                resultmap[nums2[i]] = -1
            while monotonicstack and monotonicstack[-1] < nums2[i]:
                monotonicstack.pop()
            resultmap[nums2[i]] = monotonicstack[-1] if monotonicstack else -1
            monotonicstack.append(nums2[i])
        print(resultmap)
        for x in nums1:
            resultarr.append(resultmap[x])
        return resultarr