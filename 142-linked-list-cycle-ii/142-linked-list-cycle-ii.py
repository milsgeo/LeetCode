# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        seenNode = set()
        while(curr is not None):
            if(curr in seenNode):
                return curr
            seenNode.add(curr)
            curr=curr.next
        return None