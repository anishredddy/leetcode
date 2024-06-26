# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes=[]
        
        def inorder(node):
            if node is None:
                return 
            inorder(node.left)
            nodes.append(node.val)
            inorder(node.right)
        inorder(root)

        #inorder list is done

        def build_avl(nodes):
            if len(nodes)==0:
                return None
            mid=len(nodes)//2
            node=TreeNode(nodes[mid])
            node.left=build_avl(nodes[:mid])
            node.right=build_avl(nodes[mid+1:])

            return node
        
        return build_avl(nodes)