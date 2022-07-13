# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkTree(tree1,tree2):
            if tree1 is None and tree2 is None:
                return True
            if tree1 is None or tree2 is None or tree1.val != tree2.val:
                return False
            leftTree = checkTree(tree1.left,tree2.left)
            rightTree = checkTree(tree1.right,tree2.right)
            return leftTree and rightTree
        
        if root is None:
            return False
        if root.val == subRoot.val:
            if checkTree(root,subRoot):
                return True
        
        checkLeft = self.isSubtree(root.left,subRoot)
        checkRight = self.isSubtree(root.right,subRoot)
        return checkLeft or checkRight
        
