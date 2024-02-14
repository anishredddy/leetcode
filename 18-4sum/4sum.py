class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        
        n=len(nums)

        nums.sort()



        for i in range(n):

            if i>0 and nums[i]==nums[i-1]:
                continue
            

            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                d=set()

                new_target=target-nums[i]-nums[j]
                
                for x in range(j+1,n):

                    if x>j+3 and nums[j]==nums[j-3]:
                        continue
                    if new_target-nums[x] in d:
                        if [nums[i],nums[j],nums[x],new_target-nums[x]] not in res:
                            res.append([nums[i],nums[j],nums[x],new_target-nums[x]])
                    d.add(nums[x])

        return res

                

                
