class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        new_arr = sorted(set(arr))

        hashMap={}
        
        for i in range(len(new_arr)):
            hashMap[new_arr[i]]=i+1
        
        for i in range(len(arr)):
            arr[i]=hashMap[arr[i]]
        
        return arr