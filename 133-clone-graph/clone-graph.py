"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        visited={}

        def dfs(node):
            if node in visited:
                return visited[node]
            
            visited[node]=Node(node.val)

            for nei in node.neighbors:
                visited[node].neighbors.append(dfs(nei))

            return visited[node]
        
        return dfs(node) if node else None