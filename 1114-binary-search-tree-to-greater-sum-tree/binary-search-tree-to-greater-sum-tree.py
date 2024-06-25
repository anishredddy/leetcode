# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # intuition

        # we need dfs for sure
        # we need some sort of recursion/memorisation to get value from stack

        # in inorder traversal left->node->right
        # if we take right->node-> left. we will get decreeasing order of nodes

        s=0
        def inorder(node):
            nonlocal s
            if node is None:
                return
            inorder(node.right)
            s+=node.val
            node.val=s
            inorder(node.left)
        inorder(root)
        return root