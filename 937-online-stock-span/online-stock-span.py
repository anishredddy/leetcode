class StockSpanner:

    def __init__(self):
        self.prices=[]

    def next(self, price: int) -> int:
        self.prices.append(price)
        count=0
        for p in self.prices[::-1]:
            if price>=p:
                count+=1
            else:
                break
        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)