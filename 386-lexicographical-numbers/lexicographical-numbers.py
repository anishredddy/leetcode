class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res=[]
        def dfs(i):
            if i>n:
                return
            res.append(i)
            # if i not in res:
            #     res.append(i)
            for num in range(10):
                dfs(i*10+num)
        for i in range(1,10):
            dfs(i)

        return res