# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return None
        
        
        i = 0
        current = head
        
        while current != None:
            i += 1
            current = current.next
            
        if head != None:
            
            temp = head
            
            middle = i //2 -1
            
            while middle != 0:
                middle -= 1
                head = head.next

            head.next = head.next.next
            
            return temp