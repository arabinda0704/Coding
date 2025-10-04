# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #Recursion
        # if not root:
        #     return TreeNode(val)
        # if val>root.val:
        #     root.right=self.insertIntoBST(root.right,val)
        # else:
        #     root.left=self.insertIntoBST(root.left,val)
        # return root

        #Iterative
        if not root:
            return TreeNode(val)
        
        current = root
        while True:
            # If val is greater, go right
            if val > current.val:
                if current.right:
                    current = current.right
                else:
                    current.right = TreeNode(val)
                    break
            # Otherwise, go left
            else:
                if current.left:
                    current = current.left
                else:
                    current.left = TreeNode(val)
                    break

        return root

        
          
        