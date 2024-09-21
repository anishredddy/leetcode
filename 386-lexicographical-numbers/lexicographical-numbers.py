class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res=[]
        nums=[0,1,2,3,4,5,6,7,8,9]
        def dfs(i):
            if i>n:
                return
            res.append(i)
            # if i not in res:
            #     res.append(i)
            for num in nums:
                dfs(i*10+num)
        for i in range(1,10):
            dfs(i)
            
        return res