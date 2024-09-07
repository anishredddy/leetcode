# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(
        self, head: Optional[ListNode], root: Optional[TreeNode]
    ) -> bool:
        if not root:
            return False
        result = self.dfs(root, head)
        result = result or self.isSubPath(head, root.left)
        result = result or self.isSubPath(head, root.right)
        return result

    def dfs(self, node: Optional[TreeNode], head: Optional[ListNode]) -> bool:
        if not head:
            return True
        if not node:
            return False
        result = False
        if node.val == head.val:
            # Continue searching in both left and right subtrees
            result = self.dfs(node.left, head.next)
            result = result or self.dfs(node.right, head.next)
        return result