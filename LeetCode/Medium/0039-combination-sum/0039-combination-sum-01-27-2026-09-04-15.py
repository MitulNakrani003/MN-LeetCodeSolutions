class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        finalresult = []
        def dfs(candicates,target, already):
            for x in candidates:
                arr = [] + already
                result = target - x
                if result == 0:
                    arr.append(x)
                    arr.sort()
                    if arr not in finalresult:
                        finalresult.append(arr)
                elif result > 0:
                    arr.append(x)
                    dfs(candicates,result, arr)

        dfs(candidates,target,[])
        print(finalresult)
        return finalresult


                    