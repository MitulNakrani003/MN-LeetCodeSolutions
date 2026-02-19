class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)-1
        for i in range(len(matrix)//2):
            for j in range(len(matrix)):
                matrix[i][j], matrix[n-i][j] =  matrix[n-i][j], matrix[i][j]
        # print(matrix)
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):                
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # print(matrix)
        