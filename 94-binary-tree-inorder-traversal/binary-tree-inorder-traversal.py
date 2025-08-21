
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def solve(self, root: Optional[TreeNode],inn : List[int]):
        if not root:
            return
        self.solve(root.left,inn)
        inn.append(root.val)
        self.solve(root.right,inn)
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inn=[]
        self.solve(root,inn)
        return inn