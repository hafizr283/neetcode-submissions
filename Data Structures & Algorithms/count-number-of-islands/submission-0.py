class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)
        col=len(grid[0])
        def validIdx(i,j):
            if 0<=i<row and 0<=j<col:
                return True
            return False
        del_pos = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(i,j,vis,grid):
            if not validIdx(i,j):
                return;
            vis[i][j]=True
            for x in del_pos:
                ii=x[0]+i
                jj=x[1]+j
                if validIdx(ii,jj) and not vis[ii][jj] and grid[ii][jj]=='1':
                    vis[ii][jj]=True
                    dfs(ii,jj,vis,grid)
        vis=[]
        for _ in range(row):
            vis.append([False]*col)
        ans=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1' and not vis[i][j]:
                    ans+=1
                    dfs(i,j,vis,grid)
        return ans


