# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #using hare and tortise algo
        if not (head and head.next and head.next.next):
            return False
        slow=head.next
        fast=head.next.next
        while fast and fast.next:
            if slow==fast:
                return True
            slow=slow.next
            fast=fast.next.next
        return False