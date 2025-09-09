# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if len(nums)==0:
            return head
        seen=set(nums)
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        while prev.next:
            if prev.next.val in seen:
                prev.next = prev.next.next   # delete curr
            else:
                prev = prev.next            # keep curr

        return dummy.next