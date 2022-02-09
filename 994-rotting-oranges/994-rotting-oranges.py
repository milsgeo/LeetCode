class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue=deque()
        time=0
        fresh=0
        rows=len(grid)
        cols=len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh +=1
                if(grid[r][c]==2):
                    queue.append([r,c])
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
                    
        while queue and fresh >0:
            for i in range(len(queue)):
                #popping the coordinates of the rotting  oranges
                r,c = queue.popleft()
                for dr, dc in directions:
                    row,col=dr+r,dc+c
                    #if it is fresh, make it rotten
                    if(row < 0 or row==len(grid) or (col <0 or col==len(grid[0])) or grid[row][col]!=1):
                        continue
                    #making that cell rotten
                    grid[row][col]=2
                    queue.append([row,col])
                    fresh -=1
            time +=1
        return time if fresh==0 else -1