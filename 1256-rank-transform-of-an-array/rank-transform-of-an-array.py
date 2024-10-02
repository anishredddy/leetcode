class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        new_arr = sorted(set(arr))

        for i in range(len(arr)):
            count=self.binary_search(new_arr,arr[i])
            arr[i]=count+1
        return arr

    def binary_search(self,arr,num):
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==num:
                return mid
            elif arr[mid]<num:
                low=mid+1
            else:
                high=mid-1
        return low