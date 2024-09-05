class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_m=sum(rolls)
        m=len(rolls)
        sum_n=(mean*(m+n))-sum_m

        #now we need a list of n elements such that the average is sum_n
        rem=sum_n//n
        # print(rem)
        quo=sum_n%n
        # print(quo)
        # print(sum_n)
        if sum_n>n*6 or rem<=0:
            print("hi")
            return []
        if sum_n%n==0:
            return [rem]*n
        res=[rem]*n
        for i in range(n):
            while res[i]+1<=6 and quo:
                res[i]+=1
                quo-=1
            if quo==0:
                break
        return res