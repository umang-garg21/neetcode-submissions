# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS

        lst =[]
        from collections import deque
        q= deque()

        # append (Node, depth)
        # pop left and append right 
        # grow the list till depth changes

        if root is None:
            return lst
        
        cur_depth= 1
        q.append((root,cur_depth))

        cur_lst=[]
        while q:
            #print("cur depth", cur_depth)
            ele, depth = q.popleft()
            #print("ele", ele.val)
            if depth == cur_depth:
                cur_lst.append(ele.val)
            else:
                lst.append(cur_lst)
                cur_depth+=1 
                cur_lst=[ele.val]
            
            if ele.left is not None:
                q.append((ele.left, cur_depth+1))
            if ele.right is not None:
                q.append((ele.right, cur_depth+1))
            
        lst.append(cur_lst)
        return lst
            




        

