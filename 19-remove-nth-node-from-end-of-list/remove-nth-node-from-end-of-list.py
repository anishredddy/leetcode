class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        # Advance the first pointer by n + 1 positions
        for i in range(n + 1):
            first = first.next

        # Move both pointers until the first pointer reaches the end
        while first is not None:
            first = first.next
            second = second.next

        # Now, the second pointer is at the node before the one to be removed
        second.next = second.next.next

        return dummy.next  # Return the modified head