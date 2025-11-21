class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        fuelcount = 0
        for x in nums:
            if x == candidate:
                fuelcount+=1
            else:
                if fuelcount == 0:
                    candidate = x
                    fuelcount+=1
                elif fuelcount > 0:
                    fuelcount-=1
        print(candidate)
        
        count = 0
        for x in nums:
            if x == candidate:
                count+=1
        if count > int((len(nums)/2)):
            return candidate
