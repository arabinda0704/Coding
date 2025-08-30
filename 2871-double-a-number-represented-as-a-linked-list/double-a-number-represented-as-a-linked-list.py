# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        prev=None
        curr=head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head= self.reverse(head)
        temp=head
        prev=None
        carry=0
        while temp:
            new_val = (2 * temp.val + carry)
            temp.val = new_val % 10
            carry = new_val // 10
            prev=temp
            temp=temp.next
        if carry:
            prev.next=ListNode(carry)
        
    
        return self.reverse(head)
        