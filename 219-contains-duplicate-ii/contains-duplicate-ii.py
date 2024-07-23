class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s=defaultdict(list)
        for ind,num in enumerate(nums):
            if num in s:
                for n in s[num]:
                    if abs(ind-n)<=k:
                        return True
            s[num].append(ind)
        return False