# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        l1 = []
        summ = 0
        while curr:
            if curr.val == 0:
                if curr != head:
                    l1.append(summ)
                    summ = 0
            else:
                summ += curr.val
            curr = curr.next

        dummy = ListNode(0)  # Dummy starter node

        temp = dummy
        for val in l1:
            temp.next = ListNode(val)  
            temp = temp.next  
        return dummy.next
