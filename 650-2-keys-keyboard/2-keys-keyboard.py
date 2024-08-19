class Solution:
    def minSteps(self, n: int) -> int:
        mem={}
        def helper(count,paste):
            if (count,paste) in mem:
                return mem[(count,paste)]
            if count==n:
                return 0
            if count>n:
                return float('inf')
            #paste
            res1=1+helper(count+paste,paste)

            #copy and paste
            res2=2+helper(count+count,count)

            mem[(count,paste)]=min(res1,res2)

            return min(res1,res2)
        if n==1:
            return 0
        return 1+helper(1,1)