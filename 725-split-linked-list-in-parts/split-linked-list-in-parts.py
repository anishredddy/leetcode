# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length=self.length(head)
        size=length//k
        rem=length%k
        res=[]
        for i in range(k):
            res.append(head)
            prev=head
            for i in range(size):
                if head:
                    prev=head
                    head=head.next
                else:
                    break
            if rem and head:
                rem-=1
                prev=head
                head=head.next
            if prev:
                prev.next=None
        return res
    
    def length(self,head):
        lenght=0
        while head:
            lenght+=1
            head=head.next
        return lenght