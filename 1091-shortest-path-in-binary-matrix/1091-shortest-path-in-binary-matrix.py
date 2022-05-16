class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited =set()
        q = deque()
        directions= [(0,1), (0,-1), (1,0), (-1,0), (-1,-1), (1,1), (-1,1), (1,-1)]
        
        if grid[0][0]==0:
            q.append((1,(0,0)))
            visited.add((0,0))
            
        while q:
            steps, temp=q.popleft()
            r,c = temp[0], temp[1]
            if(r,c)==(m-1, n-1):
                return steps #as we have already reached the bottom right.
            for i,j in directions:
                r_new, c_new = r+i, c+j
                if 0<=r_new<m and 0<=c_new<n and grid[r_new][c_new]==0 and (r_new, c_new)not in visited:
                    q.append((steps+1, (r_new,c_new)))
                    visited.add((r_new, c_new))
                    
        return -1