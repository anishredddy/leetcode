class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        #size= n-k+1
        def Xsum(arr):
            count=Counter(arr)
            arr.sort(key=lambda x:(-count[x],-x))
            res=0
            curr=0
            prev=None
            pos=0
            while pos<len(arr):
                if prev!=arr[pos]:
                    curr+=1
                    prev=arr[pos]
                    if curr>x:
                        break
                
                res+=arr[pos]
                pos+=1
            return res
        res=[]
        for i in range(len(nums)-k+1):
            res.append(Xsum(nums[i:i+k]))
        return res