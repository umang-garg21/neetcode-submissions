# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        max_depth=1
        if root is None:
            return 0
        else:
            left_depth, right_depth= 0,0
            #do recursive search
            if root.left is not None:
                left_depth= self.maxDepth(root.left)
            if root.right is not None:
                right_depth= self.maxDepth(root.right)
            
            max_depth= max(left_depth, right_depth)+1

        return max_depth