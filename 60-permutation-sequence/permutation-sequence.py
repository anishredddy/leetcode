class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        mem={}
        def fact(n):
            if n in mem:
                return mem[n]
            if n==0 or n==1:
                return 1
            mem[n]=n*fact(n-1)
            return mem[n]
        l=[]
        for i in range(1,n+1):
            l.append(i)
        res=""
        temp=k
        for i in range(n,0,-1):
            f=fact(i-1)
            if temp>f:
                rem=temp//f
                if temp%f==0:
                    rem-=1
            else:
                rem=0
            if rem>0:
                temp-=fact(i-1)*rem
            if rem>=len(l):
                rem=len(l)-1
            res+=str(l[rem])
            l.pop(rem)
        return res