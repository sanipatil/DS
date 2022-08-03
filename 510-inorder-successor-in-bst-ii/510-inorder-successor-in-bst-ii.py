"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if node is None:
            return None
        if node.right:
            node = node.right
            if node.left:
                while node.left:
                    node = node.left
            return node
        else:
            while node.parent:
                if node.parent.val > node.val:
                    return node.parent
                node = node.parent