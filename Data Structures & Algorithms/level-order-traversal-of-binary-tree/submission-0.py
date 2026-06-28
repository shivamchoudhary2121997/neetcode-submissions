# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
          return_list = []
          bfs = deque()
          bfs.append(root)
          while bfs:
            level = []
            qlen = len(bfs)
            for i in range(qlen):
                node = bfs.popleft()
                if node:
                    level.append(node.val)
                    bfs.append(node.left)
                    bfs.append(node.right)
            if level:
                return_list.append(level)
          return return_list

            