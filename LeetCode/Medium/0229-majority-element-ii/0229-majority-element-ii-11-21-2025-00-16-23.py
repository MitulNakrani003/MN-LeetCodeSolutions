class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        can1 = can2 = cnt1 = cnt2 = 0
        for x in nums:
            if x == can1:
                cnt1+=1
            elif x == can2:
                cnt2+=1
            elif cnt1 == 0:
                can1=x
                cnt1+=1
            elif cnt2 == 0:
                can2=x
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
        print(can1,can2)
        cou1, cou2 = 0, 0

        for x in nums:
            if x == can1:
                cou1+=1
            elif x == can2:
                cou2+=1
        
        result = []
        if cou1 > len(nums)//3:
            result.append(can1)
        if cou2 > len(nums)//3:
            result.append(can2)
        return result
        

