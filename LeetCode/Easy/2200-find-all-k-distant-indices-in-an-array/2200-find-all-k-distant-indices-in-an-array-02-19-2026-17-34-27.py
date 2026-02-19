class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        keypositions = [i for i in range(len(nums)) if nums[i]==key]
        positionchecked = -1
        result = set()
        iterval = 0
        while iterval < len(keypositions):
            startpos = keypositions[iterval]-k if keypositions[iterval]-k >= 0 else 0
            endpos = keypositions[iterval]+k if keypositions[iterval]+k < len(nums) else len(nums)-1

            print(keypositions[iterval],startpos,endpos)
            for x in range(startpos,endpos+1):
                result.add(x)
            iterval+=1
        print(result)
        return list(result)
            
            


            
            

