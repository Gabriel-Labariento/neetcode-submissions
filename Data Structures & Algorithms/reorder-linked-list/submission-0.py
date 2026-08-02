# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Get the length of the list
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        
        # Get the halfway point
        half = n // 2
        i = 0
        node = head
        while i <= half:
            if n % 2 == 0 and i == half - 1:
                prev = node
                node = node.next
                prev.next = None
                break
            
            if n % 2 == 1 and i == half:
                prev = node
                node = node.next
                prev.next = None
                break
            i += 1
            node = node.next

        # Determine halves based on divisibility
        lh = head
        rh = node
        
        # Reverse the right half
        rh = self.reverseList(rh)
        while rh:
            ltemp, rtemp = lh.next, rh.next
            lh.next = rh
            rh.next = ltemp
            lh, rh = ltemp, rtemp

        
    def reverseList(self, head) -> newHead:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev

            

