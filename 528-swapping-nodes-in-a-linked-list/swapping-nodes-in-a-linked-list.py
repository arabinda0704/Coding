# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nums=[]
        temp=head
        while temp:
            nums.append(temp.val)
            temp=temp.next
        n=len(nums)
        nums[k-1],nums[k*-1]=nums[k*-1],nums[k-1]
        dummy=ListNode(0)
        tail=dummy
        for val in nums:
            tail.next=ListNode(val)
            tail=tail.next
        return dummy.next

        