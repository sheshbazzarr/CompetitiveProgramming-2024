# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum=0
        
        def depthFirstSeach(root):
            if root is None:
                return 0
            
            leftRoot=root.left
            rightRot=root.right
            
            if root.left:    
                leftLeave_ofLeft=root.left.left
                rightLeave_ofLeft=root.left.right
                value_ofLeft=root.left.val
                if leftLeave_ofLeft == None and rightLeave_ofLeft == None:
                    self.sum+=value_ofLeft      
                    
            depthFirstSeach(leftRoot)
            depthFirstSeach(rightRot)
            
        depthFirstSeach(root)
        return self.sum