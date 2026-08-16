class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        vis = [False] * numCourses
        recPath = [False] * numCourses
        ans = []
        adj=[[] for _ in range(numCourses)]
        for x,y in prerequisites:
            adj[y].append(x)
        def dfs(ver):
            # ans.append(ver)
            vis[ver]=True
            recPath[ver]=True
            for child in adj[ver]:
                if recPath[child] and vis[child]:
                    return False
                if not vis[child]:
                    vis[child]=True
                    recPath[child]=True
                    if not dfs(child):
                        return False
                
            recPath[ver]=False
            ans.append(ver)
            return True
        a=True
        for i in range(numCourses):
            if not vis[i]:

                a&=dfs(i)
        if a:
            return ans[::-1]
        return []


