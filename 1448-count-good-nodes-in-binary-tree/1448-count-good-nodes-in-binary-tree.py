# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.output=0
        def dfs(node, max_path):
            if not node:
                return 
            if max_path <= node.val:
                self.output +=1
            if node.right:
                dfs(node.right, max(node.val, max_path))
            if node.left:
                dfs(node.left, max(node.val, max_path))
        dfs(root, float("-inf"))
        return self.output