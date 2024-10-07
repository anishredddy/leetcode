class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n1,n2=len(word1),len(word2)
        good=[-1]*(n2+1)
        good[n2]=n1

        r=n1-1
        for i in range(n2-1,-1,-1):
            while r>=0 and word1[r]!=word2[i]:
                r-=1
            good[i]=r
            if r<0:
                break
            r-=1
        res=[]
        used=False
        r=0
        print(good)
        for i in range(n1):
            if r>=n2:
                break
            if word1[i]==word2[r]:
                res.append(i)
                r+=1
                continue
            if not used and good[r+1]>=i+1:
                res.append(i)
                used=True
                r+=1
                continue
        print(res)
        if len(res)!=n2:
            return []
        return res