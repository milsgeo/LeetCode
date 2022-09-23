class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        n,m =len(matrix), len(matrix[0])
        
        def binarySearch(row):
            l,r=0,m-1
            
            
            while l<=r:
                mid=(l+r)//2
                if(matrix[row][mid]==target):
                    return True
                elif (matrix[row][mid]>target):
                    r=mid-1
                else:
                    l=mid+1
            return False
        
        for row in range(n):
            if binarySearch(row):
                return True
        return False