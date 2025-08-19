# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        prev=None
        
        while curr:
            nextNode=curr.next
            curr.next=prev
            prev=curr
            curr=nextNode
        return prev
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head1 = self.reverse(head)
        maxx=head1.val
        curr=head1
        while curr and curr.next:
            if curr.next.val<maxx:
                curr.next=curr.next.next
            else:
                maxx=curr.next.val
                curr=curr.next
        head2=self.reverse(head1)
        return head2
            
        

         

        