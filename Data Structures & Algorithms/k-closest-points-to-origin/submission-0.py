class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        value_idx=[]
        for i in range(len(points)):
         x=points[i][0]
         y=points[i][1]
         value_idx.append((x**2+y**2,i))

         heapq.heapify(value_idx)
         ans=[]
        for _ in range(k):
            _,x = heapq.heappop(value_idx)
            ans.append(points[x])
            
        return ans

    