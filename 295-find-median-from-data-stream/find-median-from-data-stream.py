class MedianFinder:

    def __init__(self):
        self.left=[]
        self.right=[]
        self.l_len=0
        self.r_len=0

    def addNum(self, num: int) -> None:
        if len(self.left)<=len(self.right):
            if len(self.left)==0:
                heapq.heappush(self.left,-num)
            elif num<=self.right[0]:
                heapq.heappush(self.left,-num)
            else:
                heapq.heappush(self.left,-1*heapq.heappop(self.right))
                heapq.heappush(self.right,num)
            self.l_len+=1
        else:
            if num>=-1*self.left[0]:
                heapq.heappush(self.right,num)
            else:
                heapq.heappush(self.right,-1*heapq.heappop(self.left))
                heapq.heappush(self.left,-1*num)
            self.r_len+=1

    def findMedian(self) -> float:
        if self.l_len>self.r_len:
            return -1*self.left[0]
        elif self.r_len>self.l_len:
            return self.right[0]
        else:
            return (-1*self.left[0]+self.right[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()