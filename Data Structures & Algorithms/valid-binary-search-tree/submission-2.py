# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # recursive BST check
        if root is None:
            return True
        
        def dfs(node, left, right):
            
            if node is None:
                return True

            if not (node.val> left and node.val< right):
                return False
            
            if not (dfs(node.left, left, node.val) and dfs(node.right, node.val, right)):
                return False

            return True

        return dfs(root, float("-inf"), float("inf"))



            



        