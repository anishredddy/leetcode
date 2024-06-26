class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        s = set()
        def dfs(i,count):
            if i == len(nums):
                return 1
            res = dfs(i + 1,count)

            if not count[(nums[i] - k)] and not count[(nums[i] + k)]:
                count[(nums[i])]+=1
                res += dfs(i + 1,count)
                count[nums[i]]-=1
            return res

        return dfs(0,defaultdict(int))-1
