# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        prev=head
        curr=head.next
        while curr:
            gcd=self.gcd(prev.val,curr.val)
            new_node=ListNode(gcd)
            prev.next=new_node
            new_node.next=curr
            prev=curr
            curr=curr.next
        return head
    def gcd(self,num1,num2):
        if num2==0:
            return num1
        else:
            return self.gcd(num2,num1%num2)