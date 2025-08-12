# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        l1=[]
        curr=head
        while curr:
            l1.append(curr.val)
            curr=curr.next
        decimal=0
        for b in l1:
            decimal = (decimal << 1) | b
        return decimal
        
        