# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        out=[]
        levelList= deque()
        if root is None:
            return []
        
        node_queue=deque([root,None])
        reverse=True
        
        while len(node_queue)>0:
            curr=node_queue.popleft()
            
            if curr:
                if reverse:
                    levelList.append(curr.val)
                else:
                    levelList.appendleft(curr.val)
                if curr.left:
                    node_queue.append(curr.left)
                if curr.right:
                    node_queue.append(curr.right)
            else:
                #finishing one level
                out.append(levelList)
                
                if len(node_queue)>0:
                    node_queue.append(None)
                #neddxt level
                levelList=deque()
                reverse = not reverse
                
        return out