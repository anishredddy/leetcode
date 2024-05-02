# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root=root
        self.res=[]

        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            self.res.append(root.val)
            dfs(root.right)

        dfs(root)

        self.ptr=0
        self.len=len(self.res)

    def next(self) -> int:
        self.ptr+=1
        return self.res[self.ptr-1]  

    def hasNext(self) -> bool:
        if self.ptr<=self.len-1:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()