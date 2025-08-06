# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Data Replacement
        if not head or not head.next or not head.next.next:
            return head
        l1=[]
        temp=head
        while temp:
            l1.append(temp.val)
            if not temp.next:
                break
            temp=temp.next.next
        temp=head.next
        while temp:
            l1.append(temp.val)
            if not temp.next:
                break
            temp=temp.next.next
        i=0
        temp=head
        while temp and i<len(l1):
            temp.val=l1[i]
            i+=1
            temp=temp.next
        return head

