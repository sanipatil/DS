# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = []
        def inorderTrav(node):
            if node is None:
                return 
            inorderTrav(node.left)
            result.append(node.val)
            inorderTrav(node.right)
    
        inorderTrav(root)
        for i in range(len(result)-1):
            if result[i] >= result[i+1]:
                return False
            
        return True
        
            