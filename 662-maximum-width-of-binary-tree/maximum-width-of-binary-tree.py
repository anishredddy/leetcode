# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #should do dfs
        curr=deque()
        curr.append([1,root])
        res=0
        #dfs

        while curr:
            left,right=curr[0][0],curr[-1][0]
            res=max(res,right-left+1)
            print(right-left+1)
            nxt=deque()
            while curr:
                pos,node=curr.popleft()
                if node.left:
                    nxt.append([2*pos,node.left])
                if node.right:
                    nxt.append([2*pos+1,node.right])
            curr=nxt
        return res
