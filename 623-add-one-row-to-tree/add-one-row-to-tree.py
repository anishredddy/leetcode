# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        q = deque([(root, 1)])
        while q:
            node, d = q.popleft()
            if d == depth - 1:
                node.left = TreeNode(val, left=node.left)
                node.right = TreeNode(val, right=node.right)
            else:
                if node.left:
                    q.append((node.left, d + 1))
                if node.right:
                    q.append((node.right, d + 1))
        
        return root