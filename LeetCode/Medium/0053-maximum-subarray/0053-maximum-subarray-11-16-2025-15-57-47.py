class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        left = 0
        right = 0
        currsum = nums[0]
        maxsum = currsum
        while right < len(nums)-1:
            right+=1
            indi = nums[right]
            cumu = currsum + nums[right]
            print("this")
            print(indi, cumu)
            if indi > cumu:
                left = right
                currsum = indi
            else:
                currsum = cumu
            maxsum = max(currsum, maxsum)
            print(currsum, maxsum)
        return maxsum