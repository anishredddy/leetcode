# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=head
        slow=fast=head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        if prev==head and prev.next is None:
            return None
        if prev and prev.next:
            prev.next=prev.next.next
        # if prev==head and prev.next is None:
        #     return None
        return head