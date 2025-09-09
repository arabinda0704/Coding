# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr=[]
        curr=head
        while curr:
            arr.append(curr.val)
            curr=curr.next
        def sortedArrayToBST(nums):
            if not nums:
                return None

            # Pick the middle element as the root
            mid = len(nums) // 2
            root = TreeNode(nums[mid])

            # Recursively build left and right subtrees
            root.left = sortedArrayToBST(nums[:mid])
            root.right = sortedArrayToBST(nums[mid+1:])

            return root
        return sortedArrayToBST(arr)
        

        