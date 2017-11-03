# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def findMax(nums, left, right):
    maxIndex = left
    for i in range(left + 1, right):
        if nums[maxIndex] < nums[i]:
            maxIndex = i
    return maxIndex

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return
        
        return self.buildMaximumBinaryTree(nums, 0, len(nums))
        
    def buildMaximumBinaryTree(self, nums, left, right):
        if left >= right:
            return None
        else:
            maxIndex = findMax(nums, left, right)
            node = TreeNode(nums[maxIndex])
            node.left = self.buildMaximumBinaryTree(nums, left, maxIndex)
            node.right = self.buildMaximumBinaryTree(nums, maxIndex + 1, right)
            return node
            