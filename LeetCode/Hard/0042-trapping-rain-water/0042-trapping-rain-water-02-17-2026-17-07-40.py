class Solution:
    def trap(self, height: List[int]) -> int:
        prefixMax = []
        suffixMax = []
        maxprefix = 0
        maxsuffix = 0
        for i in range(len(height)):
            if height[i] > maxprefix:
                prefixMax.append(height[i])
                maxprefix = height[i]
            else:
                prefixMax.append(maxprefix)
        for j in range(len(height)-1,-1,-1):
            if height[j] > maxsuffix:
                suffixMax.append(height[j])
                maxsuffix = height[j]
            else:
                suffixMax.append(maxsuffix)
        suffixMax.reverse()
        print(prefixMax)
        print(suffixMax)
        count = 0
        for i, x in enumerate(height):
            minheight = min(prefixMax[i],suffixMax[i])
            if x < minheight:
                count += minheight-x
        return count
        