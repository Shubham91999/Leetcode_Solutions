# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> ListNode:
        dummy = ListNode() # Creating dummy node to deal edge cases
        cur = dummy   # Points to the node we are inserting digit 

        carry = 0
        while l1 or l2 or carry: # Iterating till l1 or l2 has elements left
            v1 = l1.val if l1 else 0   # If l1 present, assign value to v1 else 0
            v2 = l2.val if l2 else 0   # If l2 present, assign value to v2 else 0

            # New digit after addition
            val = v1 + v2 + carry
            carry = val // 10  # 15 // 10 -> 1 tens digit/place
            val = val % 10     # 15 % 10 -> 5  Ones digit/place
            cur.next = ListNode(val)  # Creating new node after addition for value

            # Updating pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next


