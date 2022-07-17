# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        q = collections.deque()
        q.append(root)
        while q:
            level = []
            for i in range(len(q)):
                temp = q.popleft()
                if temp is not None:
                    level.append(temp.val)
                    if temp.left is not None:
                        q.append(temp.left)
                    if temp.right is not None:
                        q.append(temp.right)
            if level:
                result.append(level[-1])
        return result