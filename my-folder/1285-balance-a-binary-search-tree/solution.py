# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        nodes = list()
        def inorder(node):
            if not node:
                return None
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)
        inorder(root)

        def build(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            root = nodes[m]
            # IMPORTANT: reset pointers, because we're reusing old nodes
            root.left = build(l, m - 1)
            root.right = build(m + 1, r)
            return root

        return build(0, len(nodes) - 1)

