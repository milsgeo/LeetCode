class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matlen= len(matrix)
        left =0
        right = matlen-1
        
        while(left<right):
            for i in range(right-left):
                top = left
                bottom =right
                tL = matrix[top][left+i]
                matrix[top][left+i]=matrix[bottom-i][left]
                matrix[bottom-i][left]=matrix[bottom][right-i]
                matrix[bottom][right-i]=matrix[top+i][right]
                matrix[top+i][right]=tL
            
            right -=1
            left +=1
        
        