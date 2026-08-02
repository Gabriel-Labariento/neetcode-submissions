# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        maxD = 0

        stack = [root]
        while stack:
            curr = stack.pop()
            d = self.height(curr.left) + self.height(curr.right)
            maxD = max(maxD, d)
            if curr.left: stack.append(curr.left)
            if curr.right: stack.append(curr.right)
        return maxD
    
    def height(self, root):
        if not root: return 0
        l = self.height(root.left)
        r = self.height(root.right)
        return 1 + max(l, r)
        
        