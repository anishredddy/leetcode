class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        @cache
        def dfs(diff,i):
            if i==len(rods):
                return 0 if diff==0 else float("-inf")
            return max(
                dfs(diff,i+1),
                dfs(diff+rods[i],i+1)+rods[i],
                dfs((diff-rods[i]),i+1)
            )
        return dfs(0,0)