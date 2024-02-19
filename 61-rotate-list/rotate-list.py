# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #move first pointer by k+1 places
        if head is None or head.next is None:
            return head
        if k==0:
            return head
        l=1
        curr=head
        while curr.next:
            curr=curr.next
            l+=1
        k=k%l
        if k==0:
            return head
        curr=head
        for i in range(k+1):
            curr=curr.next
        ptr=head
        a=head
        prev=head
        while a.next:
            a=a.next
            prev=a
        while curr is not None:
            ptr=ptr.next
            curr=curr.next
        if ptr and prev:
            temp=ptr.next
            ptr.next=None
            prev.next=head
            head=temp
        return  head