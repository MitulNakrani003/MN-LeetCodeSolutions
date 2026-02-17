class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
            result = []
            currentsubset = []
            def backtrack(index):
                if index == len(nums):
                    result.append(currentsubset.copy())
                    return
                
                currentsubset.append(nums[index])
                backtrack(index+1)

                currentsubset.pop()
                backtrack(index+1)
            backtrack(0)
            return result


