class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row = len(grid)
        col = len(grid[0])
        q=deque()
        dist=[[0]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if grid[i][j]==0:
                    q.append([i,j])
        delx = [(1,0),(0,1),(0,-1),(-1,0)]
        while q:
            ver=q.popleft()
            # i,j=ver[0],ver[1]
            for dx,dy in delx:
                i = dx+ver[0]
                j=dy+ver[1]
                
                if 0<=i<row and 0<=j<col and grid[i][j]==2147483647:
                    q.append([i,j])
                    grid[i][j]=grid[ver[0]][ver[1]]+1
        
