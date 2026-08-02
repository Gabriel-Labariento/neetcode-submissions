# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return None

        stack = [root]
        while stack:
            curr = stack.pop()
            if self.validate(curr) == False: return False
            if curr.left: stack.append(curr.left)
            if curr.right: stack.append(curr.right)
        
        return True
    
    def validate(self, root):
        # Traverse the left tree
        # Check if every node value here is less than curr
        stack = [root.left]
        while stack:
            curr = stack.pop()
            if not curr: continue
            if curr.val >= root.val: return False
            if curr.left: stack.append(curr.left)
            if curr.right: stack.append(curr.right)
        # Traverse the right tree
        # Check if every node value here is less than curr
        stack = [root.right]
        while stack:
            curr = stack.pop()
            if not curr: continue
            if curr.val <= root.val: return False
            if curr.left: stack.append(curr.left)
            if curr.right: stack.append(curr.right)

        return True
        
