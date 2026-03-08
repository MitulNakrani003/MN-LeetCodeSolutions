class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        exists = [False] * 3
        a,b,c = target[0],target[1],target[2]
        for i,j,k in triplets:
            if i == a and j <= b and k <= c:
                exists[0] = True
            if i <=a and j == b and k <= c:
                exists[1] = True
            if i <=a and j<=b and k == c:
                exists[2] = True
        return exists[0] and exists[1] and exists[2]

