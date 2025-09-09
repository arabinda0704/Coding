# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
    
#     def goodNodes(self, root: TreeNode) -> int:
#         res=0
#         def dfs(root,max_val):
#             if not root:
#                 return
#             if root.val>=max_val:
#                 nonlocal res
#                 res+=1
#                 max_val=root.val
#             dfs(root.left,max_val)
#             dfs(root.right,max_val)
#         dfs(root,root.val)
#         return res

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return dfs(root, root.val)


def dfs(node, max_val):
    if not node:
        return 0
    
    # Check if current node is good
    good = 1 if node.val >= max_val else 0
    
    # Update max_val for children
    max_val = max(max_val, node.val)
    
    # Recurse on left and right, add results
    good += dfs(node.left, max_val)
    good += dfs(node.right, max_val)
    
    return good
    
        
        