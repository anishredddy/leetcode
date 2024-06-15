import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Sort projects by their capital requirements
        projects = sorted([[capital[i], profits[i]] for i in range(len(capital))], key=lambda x: x[0])
        
        max_heap = []
        i = 0
        n = len(capital)

        while k > 0:
            # Push all projects that can be started with the current capital into the max-heap
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1

            # If no projects can be started, break out of the loop early
            if not max_heap:
                break

            # Start the project with the highest profit
            w -= heapq.heappop(max_heap)
            k -= 1
        
        return w
