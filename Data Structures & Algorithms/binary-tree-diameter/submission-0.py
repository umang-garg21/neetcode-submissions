# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Pseudo:
        # Maintain a global var res, to be updated at end of each recursive call
        # recursively visit the left subtree and right subtree
        # get the height of left subtree, right subtree. dia = height_l + height_R
        # if dia > res: update res
        # return height = max(height_l, height_r) + 1

        res =0
        max_h =0 
        def custom_func(cur) -> int:
            # code
            nonlocal res
            h_left, h_right =0,0 
            if cur.left is not None:
                # get left height
                h_left = custom_func(cur.left)
            if cur.right is not None:
                h_right = custom_func(cur.right)
            #print("here h_left, h_right", h_left)
            max_dia = h_left + h_right
            if max_dia > res:
                res = max_dia

            return max(h_left, h_right)+1

        if root is None:
            return 0

        max_h= custom_func(root)

        return res


        


        


            

