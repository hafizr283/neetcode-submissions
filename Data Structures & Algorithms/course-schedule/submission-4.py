class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        vis=[False]*numCourses
        path=[False]*numCourses
        adj=[[] for _ in range(numCourses)]
        for x,y in prerequisites:
            adj[y].append(x)
        def dfs(ver,par):
            vis[ver]=True
            path[ver]=True
            for child in adj[ver]:
                if not vis[child]:
                    vis[child]=True
                    path[child]=True
                    if not dfs(child,ver):
                        return False
                if vis[child] and path[child]:
                    return False
            path[ver]=False
            return True
        a=True
        for i in range(numCourses):
            if not vis[i]:
                a&=dfs(i,-1)
        return a




                                                                                                                                                                                                    
