# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def collectLeaves(node):
            if node is None:
                return []
            elif node.left is None and node.right is None:
                return [node.val]
            else:
                return collectLeaves(node.left) + collectLeaves(node.right)
        
        def removeLeaves(node):
            if node is None:
                return None
            elif node.left is None and node.right is None:
                return None
            else:
                node.left = removeLeaves(node.left)
                node.right = removeLeaves(node.right)
                return node
        
        while root:
            result += [collectLeaves(root)]
            root = removeLeaves(root)
        return result