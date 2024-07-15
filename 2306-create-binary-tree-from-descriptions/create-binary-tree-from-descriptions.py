# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_map={}
        p=set()
        c=set()
        for parent,child,isLeft in descriptions:
            p.add(parent)
            c.add(child)
            if parent not in node_map:
                node_map[parent]=TreeNode(parent)

            if child not in node_map:
                node_map[child] = TreeNode(child)
            
            if isLeft:
                node_map[parent].left=node_map[child]
            else:
                node_map[parent].right=node_map[child]
        res=p.difference(c)
        return node_map[res.pop()]
        