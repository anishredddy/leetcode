class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        memo={}
        def dfs(i,j):
            if i==len(nums1) or j==len(nums2):
                return float("-inf")
            if (i,j) in memo:
                return memo[(i,j)]

            product=nums1[i]*nums2[j]

            res=max(product+dfs(i+1,j+1),
                    product,
                    dfs(i+1,j),
                    dfs(i,j+1)
                )
            
            memo[(i,j)]=res

            return memo[(i,j)]
        return dfs(0,0)