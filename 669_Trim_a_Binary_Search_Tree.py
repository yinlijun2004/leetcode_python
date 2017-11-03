# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def valid_node(node, L, R):
    return node.val <= R and node.val >= L

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if(root == None):
            return None
        
        if valid_node(root, L, R):
            result = TreeNode(root.val)
            result.left = self.trimBST(root.left, L, R)
            result.right = self.trimBST(root.right, L, R)
            return result
        elif root.val > R:
            return self.trimBST(root.left, L, R)
        else:
            return self.trimBST(root.right, L, R)
