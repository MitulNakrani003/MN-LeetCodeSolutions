class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for x in matrix:
            x.reverse()
        print(matrix)
        n = len(matrix)
        n2 = n-1
        for i in range(n):
            for j in range(n-i):
                matrix[i][j], matrix[n2-j][n2-i] = matrix[n2-j][n2-i], matrix[i][j]
        print(matrix)


        