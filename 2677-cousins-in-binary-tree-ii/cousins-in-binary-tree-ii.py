# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        q=deque()
        q.append(root)
        prev_sum=root.val
        while q:
            curr_sum=0
            for _ in range(len(q)):
                curr_node=q.popleft()
                curr_node.val=prev_sum-curr_node.val
                s=(curr_node.left.val if curr_node.left else 0)+(curr_node.right.val if curr_node.right else 0)
                
                if curr_node.left:
                    curr_sum+=curr_node.left.val
                    curr_node.left.val=s
                    q.append(curr_node.left)
                if curr_node.right:
                    curr_sum+=curr_node.right.val
                    curr_node.right.val=s
                    q.append(curr_node.right)
            prev_sum=curr_sum
        return root
