# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_map=defaultdict(list)
        nodes=[]

        temp=head
        while temp:
            node_map[temp.val].append(temp)
            nodes.append(temp.val)
            temp=temp.next
        
        nodes.sort()

        head=None
        dummy=TreeNode(0)
        prev=dummy
        while nodes:
            curr=nodes.pop(0)
            node=node_map[curr].pop()
            prev.next=node
            prev=node
        prev.next=None
        return dummy.next
            
