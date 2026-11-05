# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

    # if value of either left or right does not match then False
    # if exact match: then 2 choices: (LL, RR) or (LR, RL)
    
        if p is None and q is None:
            return True
        elif p is None and q is not None or p is not None and q is None:
            return False
        
        if p.val != q.val:
            return False
        else:
            if not (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)):
                return False
                
        return True

