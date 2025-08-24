# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # nums=[]
        # temp=head
        # while temp:
        #     nums.append(temp.val)
        #     temp=temp.next
        # n=len(nums)
        # nums[k-1],nums[k*-1]=nums[k*-1],nums[k-1]
        # dummy=ListNode(0)
        # tail=dummy
        # for val in nums:
        #     tail.next=ListNode(val)
        #     tail=tail.next
        # return dummy.next

        #Better O(1) space
        first = last = head
        temp = head
        n = 0
        
        while temp:
            n += 1
            temp = temp.next
        
        # Move first to the kth node from start
        for i in range(k - 1):
            first = first.next
        
        # Move last to the kth node from end
        last = head
        for i in range(n - k):
            last = last.next
        
        # Swap values
        first.val, last.val = last.val, first.val
        return head

        