# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Get the size of the list
        N = 0
        temp = head
        while temp:
            N += 1
            temp = temp.next
        
        target_index = N - n
        # print(f"TargetIndex: {target_index}")
        # Get the prev and after of the target node
        temp = head
        prev = None
        for i in range(target_index):
            prev = temp
            temp = temp.next
        
        if target_index == 0:
            if head.next: head = head.next
            else: return None
        else:    
            prev.next = temp.next
            temp.next = None

        return head