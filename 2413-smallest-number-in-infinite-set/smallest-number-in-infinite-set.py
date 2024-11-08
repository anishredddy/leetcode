class SmallestInfiniteSet:

    def __init__(self):
        self.count=1
        self.heap=[]

    def popSmallest(self) -> int:
        if len(self.heap)==0:
            self.count+=1
            return self.count-1
        else:
            if self.count<  self.heap[0]:
                self.count+=1
                return self.count-1
            return heapq.heappop(self.heap)

    def addBack(self, num: int) -> None:
        if self.count<=num:
            return
        if num in self.heap:
            return
        heapq.heappush(self.heap,num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)