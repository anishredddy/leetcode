class Solution:
    def specialArray(self, nums: List[int]) -> int:
        N = len(nums)
        
        freq = defaultdict(int)
        for num in nums:
            freq[min(N, num)] += 1
        
        count = 0
        for i in range(N, 0, -1):
            count += freq[i]
            if i == count:
                return i
        
        return -1