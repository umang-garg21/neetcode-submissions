# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    
        # recursive calling this function for the left subtree and right subtree
        # root initialize
        # find where the first ele of inorder occurs in prorder. split happens there
        # everything to left of mid is left subtree 

        if not preorder:
            return None
        
        index_map = {ele:i for i, ele in enumerate(inorder)}
        #print("index map", index_map)
        l,r = 0, len(preorder)-1
        pre_idx =0

        def build(l, r):

            nonlocal pre_idx
            
            if l> r:
                return None
            else:
                val= preorder[pre_idx]
                root = TreeNode(val)
                mid = index_map[val]
                pre_idx+= 1
                root.left= build(l, mid-1)
                root.right= build(mid+1, r)
            
            return root

        root= build(l, r)

        return root






        


        