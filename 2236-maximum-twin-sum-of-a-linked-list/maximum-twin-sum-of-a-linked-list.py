# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res=[]
        temp=head
        while temp:
            res.append(temp.val)
            temp=temp.next
        ans=0
        for i in range(len(res)//2):
            ans=max(ans,res[i]+res[len(res)-1-i])
        # print(res)
        return ans