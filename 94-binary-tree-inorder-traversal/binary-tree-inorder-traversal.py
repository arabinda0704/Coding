
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []  # Return an empty list when root is None
        
        # Traverse left subtree
        left = self.inorderTraversal(root.left)
        
        # Append current root value
        result = left + [root.val]
        
        # Traverse right subtree
        right = self.inorderTraversal(root.right)
        
        # Append right subtree result
        result += right
        
        return result
