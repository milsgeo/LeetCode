class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n, m = len(mat[0]), len(mat)
        t=r*c
        if n*m!=t:
            return mat

        output=[[0 for _ in range(c)] for _ in range(r)]
        k=0
        for i in range(m):
            for j in range(n):
                output[k//c][k%c]=mat[i][j]
                k+=1
        return output