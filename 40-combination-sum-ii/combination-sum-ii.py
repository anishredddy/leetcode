class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res=[]
        subset=[]

        def limited_dfs(index,target):
            if target==0:
                res.append(subset.copy())
                return
            for i in range(index,len(candidates)):
                if i>index and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break
                subset.append(candidates[i])
                limited_dfs(i+1,target-candidates[i])

                subset.pop()
        limited_dfs(0,target)
        return res