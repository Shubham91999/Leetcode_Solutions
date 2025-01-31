# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Assigning head of the linked list to current pointer
        current = head

        # Outer loop to traverse entire linked list
        while current:
            # Inner loop will check if next node present and value of next node matches the value of current node
            while current.next and current.next.val == current.val:

                # If same value found, assign address of next to next element in current nodes pointer to next
                current.next = current.next.next

            # Changing current pointer to next node    
            current = current.next
        return head