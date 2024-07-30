class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        
        if p==q:
            return p

        if p == root or q==root:
            return root

        arr1=[]
        arr2=[]

        def dfs(node,target,path):
            if node is None:
                return False
            
            if node == target:
                return path
            
            path.append(node.left)
            l=dfs(node.left,target,path)
            if l:
                return True
            path.pop()

            path.append(node.right)
            r=dfs(node.right,target,path)
            if r:
                return True
            path.pop()

            return False
        
        dfs(root,p,arr1)
        dfs(root,q,arr2)

        # print(len(arr1))
        # print(len(arr2))

        p1=p2=0
        prev=root

        while p1<len(arr1) and p2<len(arr2) and arr1[p1]==arr2[p2]:
            prev=arr1[p1]
            p1+=1
            p2+=1
        return prev
