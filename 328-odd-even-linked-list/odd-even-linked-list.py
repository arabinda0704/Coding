# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Data Replacement  O(N) Space
        # if not head or not head.next or not head.next.next:
        #     return head
        # l1=[]
        # temp=head
        # while temp and temp.next:
        #     l1.append(temp.val)
        #     if not temp.next:
        #         break
        #     temp=temp.next.next
        # temp=head.next
        # while temp:
        #     l1.append(temp.val)
        #     if not temp.next:
        #         break
        #     temp=temp.next.next
        # i=0
        # temp=head
        # while temp and i<len(l1):
        #     temp.val=l1[i]
        #     i+=1
        #     temp=temp.next
        # return head

        #Better O(1) Space
        if not head or not head.next or not head.next.next:
            return head
        odd,even=head,head.next
        evenHead=head.next
        while even and even.next:
            odd.next=odd.next.next
            even.next=even.next.next

            odd=odd.next
            even=even.next
        odd.next=evenHead
        return head


