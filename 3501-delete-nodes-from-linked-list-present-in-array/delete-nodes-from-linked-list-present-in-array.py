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
        curr=head
        while curr:
            if curr.val in seen:
                prev.next = curr.next   # delete curr
            else:
                prev = curr             # keep curr
            curr = curr.next
        return dummy.next