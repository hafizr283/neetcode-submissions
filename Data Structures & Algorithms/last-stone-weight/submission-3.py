from _heapq import heapify
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        val = [-x for x in stones]
        heapq.heapify(val)
        while len(val)>1:
            a=val[0]
            heapq.heappop(val)
            b=val[0]
            heapq.heappop(val)
            
            if a!=b:    
                heapq.heappush(val,a-b)

        return -val[0] if len(val) else 0

