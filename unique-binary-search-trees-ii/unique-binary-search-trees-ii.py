# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:        
        def bst(lower, upper):
            if upper < lower:
                return [None]
            # elif upper == lower:
            #     return [lower]
            
            possibleTrees = []
            for i in range(lower,upper+1):
                allPossibleLeftTrees = bst(lower,i-1)
                allPossibleRightTrees = bst(i+1, upper)
                print("i: ", i, " ", allPossibleRightTrees)
                
                for l in allPossibleLeftTrees:
                    for r in allPossibleRightTrees:
                        newTree = TreeNode(i)
                        newTree.left = l
                        newTree.right = r
                        possibleTrees.append(newTree)
                        
            return possibleTrees
        
        if n:
            return bst(1,n)