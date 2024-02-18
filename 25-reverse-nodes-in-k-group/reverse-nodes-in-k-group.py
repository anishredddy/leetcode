class Solution:
    def reverseKGroup(self, head, k):
        start=head
        curr=head
        count=1
        prev=None
        new_head=None
        while curr:
            if count%k==0:
                # if prev:
                #     print(" \tprev -> ",prev.val)
                temp=curr
                self.reverse(start,curr,prev)
                if new_head is None:
                    new_head=curr
                prev=start
                curr=start
                start=start.next
            count+=1
            curr=curr.next
        return new_head
    def reverse(self,start,end,left):

        if left:
            left.next=end

        prev=start
        curr=start.next

        start.next=end.next

        while prev!=end:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
            
        temp=end