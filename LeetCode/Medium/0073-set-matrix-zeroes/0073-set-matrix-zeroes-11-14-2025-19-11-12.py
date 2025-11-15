class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_row_zero = False
        first_column_zero = False

        cols = len(matrix[0])
        rows = len(matrix)

        for i in range(cols):
            if matrix[0][i] == 0:
                first_row_zero = True
                break
        for j in range(rows):
            if matrix[j][0] == 0:
                first_column_zero = True
                break

        for x in range(rows):
            for y in range(cols):
                if matrix[x][y] == 0:
                    matrix[x][0] = 0
                    matrix[0][y] = 0
        
        print(matrix)

        for x in range(1,rows):
            for y in range(1,cols):
                if (matrix[x][0] == 0 or matrix [0][y] == 0):
                    matrix[x][y] = 0
        print(matrix)

        if first_row_zero:
            for x in range(cols):
                matrix[0][x] = 0
        if first_column_zero:
            for y in range(rows):
                matrix[y][0] = 0

        
            

                
        