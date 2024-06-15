class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # starting capital w
        # capital needed to start it capital
        # profit associated with it profits
        # at most k projects can be done

        #sort based on capital

        projects=sorted([[capital[i],profits[i]] for i in range(len(capital))],key=lambda x:x[0])

        heap=[]
        i=0
        while k>0:
            while i<len(capital) and projects[i][0]<=w:
                heapq.heappush(heap,-projects[i][1])
                i+=1
            if not heap:
                break
            w-=heapq.heappop(heap)
            k-=1
        return w
                
                