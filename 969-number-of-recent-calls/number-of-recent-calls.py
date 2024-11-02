from sortedcontainers import SortedList

class RecentCounter:

    def __init__(self):
        self.l=SortedList()

    def ping(self, t: int) -> int:
        self.l.add(t)
        left=bisect_left(self.l,t-3000)
        right=bisect_right(self.l,t)
        return right-left


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)