# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root is None:
            return []  

        left = self.inorderTraversal(root.left)   

        node1 = [root.val]

        right = self.inorderTraversal(root.right)   

        return left + node1 + right 
