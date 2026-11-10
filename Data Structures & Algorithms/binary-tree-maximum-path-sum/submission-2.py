# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = root.val

        def dfs(cur):
            nonlocal res
            # split test
            left_res, right_res= 0,0
            if cur.left:
                left_res= dfs(cur.left)
                
            if cur.right:
                right_res= dfs(cur.right)

            split_res = cur.val + left_res + right_res
            left_sum= cur.val + left_res 
            right_sum= cur.val + right_res 
            res= max(res, split_res, left_sum, right_sum, cur.val)


            return max(left_sum, right_sum, cur.val)

        no_split_sum= dfs(root)

        return res


