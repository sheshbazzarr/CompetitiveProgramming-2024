# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        def dfs(root,cur_s):
            
            if not root:
                return cur_s
#             this is botom up when it find the sibliggs it will add them to the current string
            cur_s=chr(ord('a')+root.val)+cur_s
            if root.left and root.right:
                
#             derrmine which side is smaller
                return min( dfs(root.left,cur_s),
                        dfs(root.right,cur_s)
    )
            
            if root.right:
                return dfs(root.right,cur_s)
            if root.left:
                return dfs(root.left,cur_s)
             
            return cur_s
        return dfs(root,"")
            
            