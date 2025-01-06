# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#         use Floyd's Cycle Algoritgm


class Solution:
   
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        count = 0
        while head:
            if head not in seen:
                seen.add(head)
                head = head.next
            
            else:
                return True

        return False
            
