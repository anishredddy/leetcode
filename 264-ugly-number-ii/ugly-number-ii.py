class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap=[1]
        count=1
        visited=set()
        while count<n:
            num=heapq.heappop(heap)
            if num*2 not in visited:
                visited.add(num*2)
                heapq.heappush(heap,num*2)
            if num*3 not in visited:
                visited.add(num*3)
                heapq.heappush(heap,num*3)
            if num*5 not in visited:
                visited.add(num*5)
                heapq.heappush(heap,num*5)
            count+=1
        return heap[0]
            