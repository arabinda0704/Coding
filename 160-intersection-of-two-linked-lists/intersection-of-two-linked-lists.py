# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #O(n+m) time and O(1) space
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # t1,t2=headA,headB
        # while t1!=t2:
        #     t1=t1.next
        #     t2=t2.next
        #     if t1==t2:
        #         return t1 #or t2
        #     if t1==None:
        #         t1=headB
        #     if t2==None:
        #         t2=headA
        # return t1 #or t2

        #Same code shorter version
        # t1,t2=headA,headB
        # while t1!=t2:
        #     t1=t1.next if t1 else headB
        #     t2=t2.next if t2 else headA
        #     if t1==t2:
        #         return t1 #or t2
        # return t1 #or t2
        

        #Practice
        t1=headA
        t2=headB
        while t1 !=t2:
            if t1:
                t1=t1.next
            else:
                t1=headB
            if t2:
                t2=t2.next
            else:
                t2=headA
            if t1==t2:
                return t2
        return t2
    
        