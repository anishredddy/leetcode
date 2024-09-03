# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if  not any(lists):
            return None
        while len(lists)>1:
            mergedList=[]
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if i+1<len(lists) else None
                mergedList.append(self.merge(l1,l2))
            lists=mergedList
        return lists[0]

        
    def merge(self,head1,head2):
        dummy=ListNode(-1)
        temp=dummy
        while head1 and head2:
            if head1.val<head2.val:
                temp.next=head1
                temp=head1
                head1=head1.next
            else:
                temp.next=head2
                temp=head2
                head2=head2.next
        while head1:
            temp.next=head1
            temp=head1
            head1=head1.next
        while head2:
            temp.next=head2
            temp=head2
            head2=head2.next

        return dummy.next