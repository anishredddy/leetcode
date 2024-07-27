"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        q=deque()
        q.append(root)
        while q:
            for i in range(len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            #bfs done
            #now make linked list
            if len(q)>0:
                prev=q[0]
            for i in range(1,len(q)):
                curr=q[i]
                prev.next=curr
                curr.next=None
                prev=curr
        return root