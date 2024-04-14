# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # sum =  max(left,right,left+right,0)+node value
        res=float('-inf')
        flag=0
        def dfs(node):
            nonlocal res
            if node is None:
                return 0
            left=0
            if node.left:
                left=dfs(node.left)
            
            right=0
            if node.right:
                right=dfs(node.right)
            curr_sum=max(left,right,0)+node.val
            taking_3=left+right+node.val
            res=max(res,taking_3,curr_sum)
            return curr_sum
        dfs(root)
        return res