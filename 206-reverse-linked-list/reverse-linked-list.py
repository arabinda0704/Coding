# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next  # Store next node
            current.next = prev  # Reverse the link
            prev = current  # Move prev to current node
            current = next_node  # Move current to next node
        
        return prev  # New head of the reversed list


   