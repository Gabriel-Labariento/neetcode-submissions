# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.inOrderTraverse(root)[k - 1].val



    def inOrderTraverse(self, root):
        if not root: return []
        if not root.left and not root.right: return [root]
        
        arr = []
        if root.left:
            arr.extend(self.inOrderTraverse(root.left))
        
        arr.append(root)
        
        if root.right:
            arr.extend((self.inOrderTraverse(root.right)))

        return arr

        



    


