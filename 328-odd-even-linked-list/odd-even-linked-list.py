# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd=None
        even=None
        count=1
        t1=None
        t2=None

        if head is None:
            return None

        temp=head
        while temp:
            if count:
                #odd
                count=0
                if odd is None:
                    odd=temp
                if t1:
                    t1.next=temp
                t1=temp
            else:
                #even
                count=1
                if even is None:
                    even=temp
                if t2:
                    t2.next=temp
                t2=temp
            temp=temp.next
        t1.next=even
        if t2:
            t2.next=None
        return odd
            