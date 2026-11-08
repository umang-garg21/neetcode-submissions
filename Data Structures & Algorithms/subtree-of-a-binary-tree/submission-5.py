# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # We check if the current root match, if the rest of the tree is a sametree or not.
        # If yes, return True
        # else go to the child node of left subtree and see if the query is subtree of the left subtree, similarly check for   right, Do it recursively
        # Take care of edge cases:
    
        
        def issameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

            print("Here 4")
            if not p and not q:
                print("A")
                return True
            elif not p or not q:
                print("B")
                return False
            else:
                if p.val!= q.val:
                    print("C")
                    return False
                else:
                    
                    l_decision, r_decision = True, True
                    l_decision = issameTree(p.left, q.left)
                    r_decision = issameTree(p.right, q.right)

                    if l_decision and r_decision:
                        print("D")
                        return True
                    else:
                        print("E")
                        return False
            print("F")
            return True

        
        if not subRoot:
            return True

        if not root:
            return False

        print("Here 0")
        if root.val == subRoot.val:
            # check if samesubtree
            print("Here 1")
            if issameTree(root, subRoot):
                return True
        
        if root.left is not None:
            print("Here 2")
            if self.isSubtree(root.left, subRoot):
                return True
        if root.right is not None:
            print("Here 3")
            if self.isSubtree(root.right, subRoot):
                return True
    
        return False


