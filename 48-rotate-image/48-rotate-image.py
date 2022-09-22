class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)
    def transpose(self, matrix):
        n=len(matrix)
        for r in range(n):
            for c in range(r):
                matrix[r][c], matrix[c][r]=matrix[c][r], matrix[r][c]
    def reflect(self, matrix):
        n=len(matrix)
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][-j-1]=matrix[i][-j-1], matrix[i][j]
                