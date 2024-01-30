class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1:
            return 0
        a=prices[0]
        p=0
        for i in prices:
            if(i<a):
                a=i
            else:
                pro=i-a
                p=max(pro,p)
        return p