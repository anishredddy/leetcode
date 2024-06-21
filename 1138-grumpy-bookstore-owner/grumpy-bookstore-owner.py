class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # greedy
        before=0
        for i in range(len(customers)):
            if grumpy[i]==0:
                before+=customers[i]
        curr=0
        maxx=0
        print(before)#10
        for i in range(len(customers)):
            if grumpy[i]==1:
                curr+=customers[i]
            if i>=minutes and grumpy[i-minutes]==1:
                curr-=customers[i-minutes]
            maxx=max(maxx,curr)
        return maxx+before