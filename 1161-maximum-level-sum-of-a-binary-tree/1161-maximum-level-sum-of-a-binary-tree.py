# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sumlevel = {}
        q = collections.deque()
        q.append(root)
        level = 1
        maxlevel = 0
        maxsum = -math.inf
        while q:
            sumval = 0
            for i in range(len(q)):
                node = q.popleft()
                if node is not None:
                    sumval += node.val                        
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if sumval > maxsum:
                maxsum = sumval
                maxlevel = level
            level += 1
            
        return maxlevel
        
        