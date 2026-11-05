# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # recursively call the node and check left height, right height
        # if abd difference> 1, not balanced 

        if root is None:
            return True

        res= True 
        def dfs(cur):
            h_l, h_r = 0,0
            l_balanced, r_balanced= True, True
            if cur.left is not None:
                h_l, l_balanced = dfs(cur.left)
            if cur.right is not None:
                h_r, r_balanced = dfs(cur.right)

            if l_balanced is False or r_balanced is False or abs(h_l - h_r) >1:
                return max(h_l, h_r)+1, False
            
            return max(h_l, h_r)+1, True
    
        max_h, res= dfs(root)

        return res

        
        
