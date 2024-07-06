class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # number
        num=time%(n-1)
        rem=time//(n-1)
        print(num,rem)
        if rem%2==0:
            return num+1
        else:
            return n-num