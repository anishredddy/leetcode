# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        
        temp=None
        start=head
        curr=head

        som=0

        prev1=None

        count=0

        dummy=ListNode(0)
        prev=dummy

        while curr:
            if curr.val==0:
                count+=1
            if count==2:
                count=1
                new_node=ListNode(som)
                prev.next=new_node
                prev=new_node
                som=0
            som+=curr.val
            curr=curr.next
        return dummy.next

            
