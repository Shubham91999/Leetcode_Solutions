# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # # 1. Brute Force Approach using array
        # # If nothing return None
        # if not head: 
        #     None

        # # Array created to store LL elements
        # nodes = []
        # cur = head
        # while cur:
        #     nodes.append(cur)
        #     cur = cur.next

        # #print(nodes)

        # # Setting two pointers
        # i = 0
        # j = len(nodes) - 1 #last element

        # # Looping through array to reorder elements
        # while i < j:
        #     nodes[i].next = nodes[j]
        #     i += 1
        #     if i >= j:
        #         break
        #     nodes[j].next = nodes[i]
        #     j -= 1

        # nodes[i].next = None

        # 2. Reverse and Merge
        
        # Getting the middle of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reversing the second half of the linked list
        curr = slow.next
        prev = slow.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # Merging the linked list
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2