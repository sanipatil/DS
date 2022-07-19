# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        count = 0
        def inorder(node,count):
            if node is None:
                return
            if count == k:
                return
            inorder(node.left,count)
            result.append(node.val)
            count += 1
            inorder(node.right,count)

        inorder(root,count)
        return result[k-1]