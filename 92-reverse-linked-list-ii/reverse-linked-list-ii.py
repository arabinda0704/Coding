# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        curr=head
        prev=None
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        curr=head
        prev=dummy
        v=right-left
        while left-1:
            prev=curr
            curr=curr.next
            left-=1
        temp=curr
        
        while v:
            temp=temp.next
            v-=1
        last=temp.next
        temp.next=None

        newHead=self.reverse(curr)
        prev.next=newHead
        curr.next=last
        return dummy.next
        