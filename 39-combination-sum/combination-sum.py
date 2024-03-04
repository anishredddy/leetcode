class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates)==0:
            return []
        if target == 0:
            return []
        
        res=[]
        subset=[]
        def dfs(i,sum_set):
            if sum_set==target:
                if subset not in res:
                    res.append(subset.copy())
                return
            if sum_set>target:
                return
            if i>=len(candidates):
                return
            subset.append(candidates[i])
            dfs(i+1,sum_set+candidates[i])
            dfs(i,sum_set+candidates[i])

            subset.pop()
            dfs(i+1,sum_set)
        dfs(0,0)
        return res