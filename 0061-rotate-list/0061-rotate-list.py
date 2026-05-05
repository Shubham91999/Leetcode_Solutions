# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Find length and tail
        tail = head
        n = 1
        while tail.next:
            tail = tail.next
            n += 1

        k %= n
        if k == 0:
            return head

        # Find new tail: (n - k - 1) steps from head
        new_tail = head
        for _ in range(n - k - 1):
            new_tail = new_tail.next

        # Rewire
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head

        return new_head