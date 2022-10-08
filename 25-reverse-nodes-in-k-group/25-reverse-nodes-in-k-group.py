# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLinkedList(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_head, ptr=None, head
        while k:
            next_node=ptr.next
            ptr.next=new_head
            new_head=ptr
            
            ptr=next_node
            k-=1
        return new_head
    
    def reverseKGroup(self, head:ListNode, k:int) -> ListNode:
        count=0
        ptr=head
        
        while count <k and ptr:
            ptr=ptr.next
            count +=1
            
        if count ==k:
            reversedhead=self.reverseLinkedList(head,k)
            head.next=self.reverseKGroup(ptr,k)
            return reversedhead
        return head