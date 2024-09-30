class Solution:
    def reverse(self, x: int) -> int:
        rev=count=i=0
        if x<0:
            i=1
            x=-x
        while(x>0):
            rev=(rev*10)+(x%10)
            count+=1
            x=x//10
        if i:
            rev=-rev
        if rev<-2**31 or rev>2**31-1:
            return 0
        return rev