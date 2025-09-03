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
        while k-1 and curr:
            k-=1
            curr=curr.next if curr else None
        return curr
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # k=2
        # if not head or not head.next:
        #     return head
        # temp=head

        # prevnode=None
        # while temp:
        #     kthNode=self.getKthNode(temp,k)
        #     # if not kthNode:
        #     #     if prevNode:
        #     #         prevNode.next=nxt#or temp
        #     #     break
        #     #Below line also works instead of above since last node reverse or not does not matter
        #     if not kthNode:
        #         last=temp
        #         while last and last.next:
        #             last=last.next
        #         self.reverse(temp)
        #         if prevNode:
        #             prevNode.next=last
        #         break

        #     nxt=kthNode.next
        #     kthNode.next=None
        #     self.reverse(temp)
        #     if temp==head:
        #         head=kthNode
        #     else:
        #         prevNode.next=kthNode
        #     prevNode=temp
        #     temp=nxt
        # return head

        #Using recursion
        # Base case
        # if not head or not head.next:
        #     return head
        # first = head
        # second = head.next
        # first.next = self.swapPairs(second.next)

        # # Swap
        # second.next = first

        # # Return new head
        # return second

        #Practice
        # if not head or not head.next:
        #     return head
        # dummy=ListNode(0)
        # prev=dummy
        # while head and head.next:
        #     first=head
        #     second=head.next

        #     #Swapping
        #     prev.next=second
        #     first.next=second.next
        #     second.next=first

        #     prev=second.next#or first
        #     head=first.next
        # return dummy.next

        # Recursion Practice
        if not head or not head.next:
            return head
        first,second=head,head.next
        first.next=self.swapPairs(second.next)
        second.next=first
        return second



