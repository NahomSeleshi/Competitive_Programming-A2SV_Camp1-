# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        totalSum = 0
        def returnSum(node):
            nodeSum = 0
            if not node.val % 2:
                if node.left:
                    if node.left.left: nodeSum += node.left.left.val
                    if node.left.right: nodeSum += node.left.right.val
                if node.right:
                    if node.right.left: nodeSum += node.right.left.val
                    if node.right.right: nodeSum += node.right.right.val
            return nodeSum
        def DFS(node):
            nonlocal totalSum
            if not node: return 
            totalSum += returnSum(node)
            DFS(node.left)
            DFS(node.right)
        DFS(root)
        return totalSum
