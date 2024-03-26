class Solution:
    import heapq
    from collections import defaultdict
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_knums = []
        num_dict = defaultdict(int)
        for num in nums:
            num_dict[num] = num_dict[num] + 1
        # print(num_dict)
        for key, val in num_dict.items():
            heapq.heappush(sorted_knums, [-val, key])
            
        # print(sorted_knums)
        ret = []
        while k>0:
            val,key=heapq.heappop(sorted_knums)
            ret.append(key)
            k-=1
        return ret
