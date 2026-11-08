# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS with right elements first in the queue

        from collections import deque
        q= deque()

        if root is None:
            return []
        
        cur_depth=1
        q.append((root, cur_depth))
        res=[root.val]

        while q:
            
            ele, depth = q.popleft()

            if depth!=cur_depth:
                res.append(ele.val)
                cur_depth = depth

            if ele.right is not None:
                q.append((ele.right, cur_depth+1))
            if ele.left is not None:
                q.append((ele.left, cur_depth+1))

        
        return res

                


            
        








        