# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        cur = head
        while cur:
            cur = cur.next
            count += 1
        count = count // 2 # 3
        if count == 0:
            return None
        cur = head
        while cur:
            if count == 1:
                prev = cur
                cur = cur.next
                prev.next = cur.next
                cur.next = prev
            cur = cur.next
            count -= 1
        return head
        
        


