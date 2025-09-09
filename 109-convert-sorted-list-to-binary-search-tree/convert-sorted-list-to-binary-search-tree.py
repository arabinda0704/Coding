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
        # arr=[]
        # curr=head
        # while curr:
        #     arr.append(curr.val)
        #     curr=curr.next
        # def sortedArrayToBST(nums):
        #     if not nums:
        #         return None

        #     # Pick the middle element as the root
        #     mid = len(nums) // 2
        #     root = TreeNode(nums[mid])

        #     # Recursively build left and right subtrees
        #     root.left = sortedArrayToBST(nums[:mid])
        #     root.right = sortedArrayToBST(nums[mid+1:])

        #     return root
        # return sortedArrayToBST(arr)

        #Without Extra Space Better
        def listToTree(head):
            if not head:
                return None
            if not head.next:
                return TreeNode(head.val)

            # Pick the middle element as the root
            slow,fast=head,head
            prev=None
            while fast and fast.next:
                prev=slow
                slow=slow.next
                fast=fast.next.next
            prev.next=None
            root = TreeNode(slow.val)

            # Recursively build left and right subtrees
            root.left = listToTree(head)
            root.right = listToTree(slow.next)

            return root
        return listToTree(head)
            

        