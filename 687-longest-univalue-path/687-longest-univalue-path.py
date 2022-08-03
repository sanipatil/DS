# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        depth = 0
        def dfs(node):
            if node is None:
                return 0
            left = 0
            right = 0
            if node.left is not None:
                left = dfs(node.left)
                if node.left.val == node.val:
                    left += 1
                else:
                    left = 0
                
            if node.right is not None:
                right = dfs(node.right)
                if node.right.val == node.val:
                    right += 1
                else:
                    right = 0
                    
            nonlocal depth        
            depth = max(depth,left+right)
            return max(left,right)
        
        dfs(root)
        return depth