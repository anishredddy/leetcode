class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x : (x[0],-x[1]))
        hei = [h for _, h in envelopes]
        LIS=[]

        for h in hei:
            pos=bisect_left(LIS,h)
            if pos<len(LIS):
                LIS[pos]=h
            else:
                LIS.append(h)
        return len(LIS) 