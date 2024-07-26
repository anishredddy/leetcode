# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev=head
        curr=head.next        
        remove=set()
        
        while curr:
            if curr.val!=prev.val:
                prev.next=curr
                prev=curr
            else:
                remove.add(curr.val)
            curr=curr.next

        def remove_node(prev,node):
            prev.next=node.next
        
        dummy=ListNode(0,head)

        prev=dummy

        start=head

        while start:
            if start.val in remove:
                remove_node(prev,start)
            else:
                prev=start
            start=start.next


        return dummy.next