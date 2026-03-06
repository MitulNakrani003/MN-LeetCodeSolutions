class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for x in range(rowIndex):
            new_row = [0]*(len(row)+1)
            for i in range(len(row)):
                new_row[i] += row[i]
                new_row[i+1] += row[i]
            row = new_row
        return row
        
