# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        s1 = ''
        s2 = ''
        n2 = 0
        n1 = 0
        total = 0
        result = None
        current = None
        

        while l1:
            s1 = str(l1.val) + s1
            l1 = l1.next
        n1 = int(s1)

        while l2:
            s2 = str(l2.val) + s2
            l2 = l2.next
        n2 = int(s2)

        total = n1 + n2
        reversed_number = str(total)[::-1]
        i = 0
        while(i < len(reversed_number)):
            new_node = ListNode(int(reversed_number[i]))
            if result is None:
                result = new_node
                current = result
            
            else:
                current.next = new_node
                current = current.next
            i+=1
        return result

