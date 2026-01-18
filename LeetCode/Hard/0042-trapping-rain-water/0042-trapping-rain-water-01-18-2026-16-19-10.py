class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        rmax = height[r]
        lmax = height[l]
        totwater = 0
        while l < r:
            if lmax<rmax:
                l+=1
                lmax = max(lmax,height[l])
                totwater = totwater + (lmax-height[l])
            else:
                r-=1
                rmax = max(rmax,height[r])
                totwater = totwater + (rmax-height[r])
        return totwater

            