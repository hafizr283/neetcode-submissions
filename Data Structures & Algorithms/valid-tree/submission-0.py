class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edge=len(edges)
        adj=[[] for _ in range(n)]
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        vis=[False]*n
        def dfs(ver):
            for child in adj[ver]:
                if not vis[child]:
                    vis[child]=True
                    dfs(child)
        dfs(0)
        vis[0]=1
        return all(vis) and n-1==edge