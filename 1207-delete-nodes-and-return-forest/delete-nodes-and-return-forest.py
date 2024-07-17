# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res=[]

        check=set(to_delete)

        def dfs(node,prev,dirr):
            if node:
                if node.val in check:
                    if prev:
                        if dirr=='R':
                            prev.right=None
                        else:
                            prev.left=None
                    if node.right and node.right.val not in check:
                        res.append(node.right)
                    dfs(node.right,None,'U')

                    if node.left and node.left.val not in check:
                        res.append(node.left)
                    dfs(node.left,None,'U')
                    return
                else:
                    if node==root:
                        res.append(node)
                    dfs(node.left,node,'L')
                    dfs(node.right,node,'R')
        dfs(root,None,'U')
        print(res)
        return res