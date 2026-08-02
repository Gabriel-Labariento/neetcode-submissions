# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        rootVal = preorder.pop(0)
        root = TreeNode(rootVal)

        inOrderRootIndex = inorder.index(rootVal) 

        leftHalf = inorder[:inOrderRootIndex]
        rightHalf = inorder[inOrderRootIndex + 1:]

        print(f"inorder root index: {inOrderRootIndex}")
        print(f"leftHalf: {leftHalf}")
        print(f"rightHalf: {rightHalf}")

        root.left = self.buildHelper(preorder, leftHalf)
        root.right = self.buildHelper(preorder, rightHalf)

        return root

    def buildHelper(self, preorder, inorderHalf):
        if not inorderHalf or not preorder: return

        i = 0
        while preorder[i] not in inorderHalf: i += 1
        rootVal = preorder.pop(i)
        print(f"rootval: {rootVal} ")
        root = TreeNode(rootVal)

        try: 
            inOrderRootIndex = inorderHalf.index(rootVal) 
        except ValueError:
            return

        print(f"inorder root index: {inOrderRootIndex}")
        leftHalf = inorderHalf[:inOrderRootIndex] if inOrderRootIndex > 0 else None
        rightHalf = inorderHalf[inOrderRootIndex + 1:] if inOrderRootIndex + 1 < len(inorder) else None 

        print(f"leftHalf: {leftHalf}")
        print(f"rightHalf: {rightHalf}")

        root.left = self.buildHelper(preorder, leftHalf)
        root.right = self.buildHelper(preorder, rightHalf)

        return root

