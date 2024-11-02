# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node,target,include):
            if node is None:
                return 0
            count=0
            if node.val==target:
                count+=1
            count+=dfs(node.left,target-node.val,True)+dfs(node.right,target-node.val,True)

            if not include:
                count+=dfs(node.left,target,False)+dfs(node.right,target,False)
            return count
        return dfs(root,targetSum,False)