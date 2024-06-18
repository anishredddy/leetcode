class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        merged = [[profit[i], difficulty[i]] for i in range(len(profit))]
        merged = sorted(merged, key=lambda x: x[1])
        worker.sort()
        heap=[]
        res=0
        current=0
        for i in range(len(worker)):
            while current<len(worker) and worker[i]>=merged[current][1]:
                heapq.heappush(heap,-merged[current][0])
                current+=1
            if heap:
                res-=heap[0]
        return res