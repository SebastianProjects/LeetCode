# Time complexity: O(n)
# Space complexity: O(n)

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        if root == None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left) 
        return root