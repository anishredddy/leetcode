# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(root):
            if root is None: 
                return None
            
            root.left=dfs(root.left)
            root.right=dfs(root.right)

            if root.left==root.right and root.val==target:
                return None
            return root
            
        return dfs(root)
        