class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Step 1: Find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow is now at the start of the second half

        # Step 2: Reverse the second half in-place
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        # prev is now the head of the reversed second half

        # Step 3: Walk both halves, compute max twin sum
        res = 0
        left, right = head, prev
        while right:
            res = max(res, left.val + right.val)
            left = left.next
            right = right.next

        return res