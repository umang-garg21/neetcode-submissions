# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # good nodes mean that their parent nodes have to be good, cuz they lie in the path
        # recursive goodness

        # collect nodes 

        # root DFS, and if the child >= max ele encountered in the path, it is good, else not.
        res= 1
        if not root.left and not root.right:
            return res

        def dfs(cur, max_val):
            nonlocal res
            #print("Res", res)

            if cur.left is not None:
                #print("Cur left val, max val", cur.left.val, max_val)
                if cur.left.val>= max_val:
                    res+=1
                    dfs(cur.left, cur.left.val)
                else:
                    dfs(cur.left, max_val)

            if cur.right is not None:
                #print("Cur right val, max val", cur.right.val, max_val)
                if cur.right.val>= max_val:
                    res+=1
                    dfs(cur.right, cur.right.val)
                else:
                    dfs(cur.right, max_val)

            return
            
        max_val=root.val
        dfs(root, root.val)

        return res


