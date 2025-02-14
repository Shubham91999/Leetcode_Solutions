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

        # 1. Brute Force Approach using array
        # If nothing return None
        if not head: 
            None

        # Array created to store LL elements
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        #print(nodes)

        # Setting two pointers
        i = 0
        j = len(nodes) - 1 #last element

        # Looping through array to reorder elements
        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            if i >= j:
                break
            nodes[j].next = nodes[i]
            j -= 1

        nodes[i].next = None


        
        