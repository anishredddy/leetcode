# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(postorder)==0 or len(inorder)==0:
            return None
        root=TreeNode(postorder[-1])
        ind=inorder.index(postorder[-1])
        n=len(postorder)
        root.left=self.buildTree(inorder[:ind],postorder[:ind])
        root.right=self.buildTree(inorder[ind+1:],postorder[ind:n-1])
        return root