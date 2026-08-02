class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = [root]

        while q:
            level_size = len(q)      # number of nodes at this level
            level = []

            for _ in range(level_size):
                curr = q.pop(0)
                level.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            res.append(level)

        return res
