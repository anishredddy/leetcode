# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        l=deque()
        def preOrder(root):
            if root is None:
                return
            l.append(root)
            preOrder(root.left)
            preOrder(root.right)
        preOrder(root)

        #got pre order in l
        l.popleft()
        prev=root
        while l:
            node=l.popleft()
            prev.left=None
            prev.right=node
            prev=node
        prev.left=prev.right=None
        return root