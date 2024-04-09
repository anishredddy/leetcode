class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        if tickets[k]==max(tickets):
            return sum(tickets)

        res=0
        for i in range(len(tickets)):
            if i<=k:
                if tickets[i]<tickets[k]:
                    res+=tickets[i]
                else:
                    res+=tickets[k]
            else:
                if tickets[i]<tickets[k]:
                    res+=tickets[i]
                else:
                    res+=tickets[k]-1
        return res
