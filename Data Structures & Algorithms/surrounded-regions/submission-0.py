class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row,col=len(board),len(board[0])
        delx = [(1,0),(0,1),(-1,0),(0,-1)]
        q = deque()
        vis=[[False]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if board[i][j]=='O' and (i==0 or j==0 or i==row-1 or j==col-1):
                   q.append([i,j])
                   vis[i][j]=True
        
        while q:
            x,y=q.popleft()
            for dx,dy in delx:
                i=dx+x
                j=dy+y
                if 0<=i<row and 0<=j<col and not vis[i][j] and board[i][j]=='O':
                    q.append([i,j])
                    vis[i][j]=True
        for i in range(row):
            for j in range(col):
                if not vis[i][j] and board[i][j]=='O':
                    board[i][j]='X'
        
        
