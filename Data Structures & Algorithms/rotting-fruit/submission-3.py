class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        q=deque()
        fresh=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    q.append([i,j])
                elif grid[i][j]==1:
                    fresh+=1
        delx = [(1,0),(0,1),(0,-1),(-1,0)]
        
        ans = 0
        while q:
            for _ in range(len(q)):
                x,y =q.popleft()
                for dx,dy in delx:
                    i = x+dx
                    j=y+dy
                    if 0<=i<row and 0<=j<col and grid[i][j]==1:
                        fresh-=1
                        grid[i][j]=2
                        q.append([i,j])
            ans+=1
        if fresh==0:
            return ans-1 if ans>0 else 0

        else:
            return -1