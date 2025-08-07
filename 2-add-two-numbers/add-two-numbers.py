# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1=l1
        t2=l2
        dummy=ListNode()
        cur=dummy
        carry=0
        while t1 or t2:
            summ=carry
            if t1:
                summ+=t1.val
            if t2:
                summ+=t2.val
            new=ListNode(summ%10)
            carry=summ//10
            cur.next=new

            cur=cur.next
            if t1:
                t1=t1.next
            if t2:
                t2=t2.next
        if carry:
            new=ListNode(carry)
            cur.next=new
        #     cur=cur.next
        # cur.next=None
        return dummy.next

        