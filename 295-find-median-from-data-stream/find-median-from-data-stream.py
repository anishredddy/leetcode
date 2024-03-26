class MedianFinder:

    def __init__(self):
        self.left=[]
        self.right=[]

    def addNum(self, num: int) -> None:
        if len(self.left)<=len(self.right):
            if len(self.left)==0:
                heapq.heappush(self.left,-num)
            elif num<=self.right[0]:
                heapq.heappush(self.left,-num)
            else:
                heapq.heappush(self.left,-1*heapq.heappop(self.right))
                heapq.heappush(self.right,num)
        else:
            if num>=-1*self.left[0]:
                heapq.heappush(self.right,num)
            else:
                heapq.heappush(self.right,-1*heapq.heappop(self.left))
                heapq.heappush(self.left,-1*num)

    def findMedian(self) -> float:
        if len(self.left)>len(self.right):
            return -1*self.left[0]
        elif len(self.right)>len(self.left):
            return self.right[0]
        else:
            return (-1*self.left[0]+self.right[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()