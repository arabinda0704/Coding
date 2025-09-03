# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev

    def getKthNode(self,head,k):
        curr=head
        while k-1:
            k-=1
            curr=curr.next if curr else None
        return curr



    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp=head

        prev=None
        while temp:
            kthnode=self.getKthNode(temp,k)
            if not kthnode:
                if prev:
                    prev.next=nxt
                break
            nxt=kthnode.next
            kthnode.next=None
            self.reverse(temp)
            if temp==head:
                head=kthnode
            else:
                prev.next=kthnode
            prev=temp
            temp=nxt
        return head


        