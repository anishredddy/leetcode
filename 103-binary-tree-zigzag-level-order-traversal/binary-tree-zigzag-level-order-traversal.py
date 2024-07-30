# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q=deque()
        q.append(root)
        res=[]
        flag=0
        while q:
            curr=[]
            for i in range(len(q)):
                node=q.popleft()
                curr.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if flag==0:
                res.append(curr)
                flag=1
            elif flag==1:
                res.append(curr[::-1])
                flag=0
        return res