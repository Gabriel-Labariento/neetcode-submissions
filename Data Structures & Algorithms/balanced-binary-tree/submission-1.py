# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        if not root: return True

        stack = []
        stack.append(root)

        while stack:
            currNode = stack.pop(-1)
            if currNode.left is not None:
                stack.append(currNode.left)
            if currNode.right is not None:
                stack.append(currNode.right)
            if abs(self.heightdfs(currNode.right) - self.heightdfs(currNode.left)) > 1:
                isBalanced = False
        
        return isBalanced

    def heightdfs(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        
        left_height = self.heightdfs(root.left)
        right_height = self.heightdfs(root.right)
        
        return 1 + max(left_height, right_height)