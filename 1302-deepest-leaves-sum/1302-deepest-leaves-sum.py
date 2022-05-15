# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        deepest_level_sum=depth=0
        stack=[(root,0)]
        
        while stack:
            node, current_depth=stack.pop()
            if node.left is None and node.right is None:
                if depth < current_depth:
                    deepest_level_sum = node.val
                    depth= current_depth
                elif depth == current_depth:
                    deepest_level_sum += node.val
                    
            else:
                if node.right:
                    stack.append((node.right, current_depth+1))
                if node.left:
                    stack.append((node.left, current_depth+1))
        
        return deepest_level_sum