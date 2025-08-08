# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # seen = set()
        # cur = head
        # while cur:
        #     if cur in seen:
        #         return cur
        #     seen.add(cur)
        #     cur = cur.next
        # return None


        # Better Floyds
        if not head:
            return
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        slowNew=head
        
        while slow.next:
            if slow==slowNew:
                return slow
            slow=slow.next
            slowNew=slowNew.next
            
        # return
        
          
        