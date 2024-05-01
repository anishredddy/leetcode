# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0:
            return None
        if len(preorder)==1:
            return TreeNode(preorder[0])
        curr=preorder[0]
        pos=len(preorder)
        for ind,num in enumerate(preorder):
            if num>curr:
                pos=ind
                break
        node=TreeNode(curr)
        # print("left:",preorder[1:pos])
        node.left=self.bstFromPreorder(preorder[1:pos])
        node.right=self.bstFromPreorder(preorder[pos:])

        return node