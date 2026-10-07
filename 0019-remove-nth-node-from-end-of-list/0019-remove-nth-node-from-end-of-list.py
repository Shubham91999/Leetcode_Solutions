class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        left = dummy
        right = dummy

        for _ in range(n):
            right = right.next

        while right.next:
            right = right.next
            left = left.next
            
        left.next = left.next.next
        return dummy.next


