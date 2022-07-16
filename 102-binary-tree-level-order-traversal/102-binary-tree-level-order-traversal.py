# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        q = collections.deque()
        q.append(root)
        while q:
            levels = []
            for i in range(len(q)):
                node = q.popleft()
                if node is not None:
                    levels.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if len(levels) != 0:
                result.append(levels)
        return result
        