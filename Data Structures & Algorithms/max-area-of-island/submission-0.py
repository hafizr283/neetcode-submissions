class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        vis=[[False]*col for _ in range(row)]
        def valid(i,j):
            return 0<=i<row and 0<=j<col
        def dfs(i,j):
            if not valid(i,j) or  vis[i][j] or not grid[i][j]:
                return 0
            vis[i][j]=1
            a=dfs(i+1,j)
            b=dfs(i,j+1)
            c=dfs(i-1,j)
            d=dfs(i,j-1)
            return 1+a+b+c+d
        ans=0
        for i in range(row):
            for j in range(col):
                if grid[i][j] and not vis[i][j]:
                    ans=max(ans,dfs(i,j))
        return ans
