# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def height(root):
            if not root:
                return [True, 0]
            lefth = height(root.left)
            righth = height(root.right)
            balanced = lefth[0] and righth[0] and (abs(lefth[1]-righth[1])<=1)
            return [balanced, 1+max(lefth[1], righth[1])]
        rooth = height(root)
        return rooth[0]