class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        startRow=0
        endRow = len(matrix)-1
        startCol=0
        endCol=len(matrix[0])-1
        result=[]
        
        while(startRow <= endRow and startCol <= endCol):
            #Traversing the top row left to right
            for col in range(startCol, endCol+1):
                result.append(matrix[startRow][col])
                
            #Traversing the last Col top to bottom and excluding the top right corner
            for row in range(startRow+1, endRow+1):
                result.append(matrix[row][endCol])
                
            #Traversing the last row right to left excluding the bottom right corner
            for col in reversed(range(startCol,endCol)):
                if(startRow==endRow):
                    break                
                result.append(matrix[endRow][col])
                
            #Traversing the first col exclusing the bottom left and otp left corners
            for row in reversed(range(startRow+1,endRow)):
                if(startCol==endCol):
                    break
                result.append(matrix[row][startCol])
                
            startRow +=1
            endRow -=1
            startCol +=1
            endCol -=1
            
        return result