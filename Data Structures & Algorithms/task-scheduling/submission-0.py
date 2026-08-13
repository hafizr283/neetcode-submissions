class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        l=Counter(tasks)
        maxHeap = [-x for x in l.values()]
        heapq.heapify(maxHeap)
        q=deque()
        time = 0
        while q or maxHeap:
            time+=1
            if maxHeap:
                x=heapq.heappop(maxHeap)
                if x+1:
                    q.append([x+1,time+n])
            if q:
                if q[0][1]==time:
                    heapq.heappush(maxHeap,q[0][0])
                    q.popleft()

        
        return time