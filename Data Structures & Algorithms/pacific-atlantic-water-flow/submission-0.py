class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row,col=len(heights),len(heights[0])
        pac=[[False]*col for _ in range(row)]
        atlan = [[False]*col for _ in range(row)]
        q=deque()
        delx=[(1,0),(0,1),(0,-1),(-1,0)]
        def bfs(grid,vis):
            for x,y in grid:
                q.append([x,y])
                vis[x][y]=1
            while q:
                x,y =q.popleft()
                for dx,dy in delx:
                    i=x+dx
                    j=y+dy
                    if 0<=i<row and 0<=j<col and not vis[i][j] and heights[i][j]>=heights[x][y]:
                        vis[i][j]=1
                        q.append([i,j])
        l1,l2=[],[]
        for i in range(row):
            for j in range(col):
                if i==0 or j==0:
                    l1.append([i,j])
                if i==row-1 or j==col-1:
                    l2.append([i,j])
        bfs(l1,atlan)
        bfs(l2,pac)
        ans=[]
        for i in range(row):
            for j in range(col):
                if atlan[i][j] and  pac[i][j]:
                    ans.append([i,j])
        return ans
        


