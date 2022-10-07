# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        i = 0
        current = head
        
        while current != None:
            i += 1
            current = current.next
            
        if head != None:
            
            temp = head
            
            middle = i //2
            
            while middle != 0:
                temp = temp.next
                middle -= 1
        
            return temp