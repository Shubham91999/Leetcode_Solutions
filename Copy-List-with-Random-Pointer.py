"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 1. HashMap
        # oldToCopy = {None: None} # Initializing with None to handle edge case where node's random pointer is None
        # # First Pass to create list of new nodes
        # cur = head
        # while cur:
        #     copy = Node(cur.val)
        #     oldToCopy[cur] = copy
        #     cur = cur.next
        # # After above pass, hashmap will contain mappings of each original node to its corresponding copied node, but next and random pointers of new nodes are still none
    
        # # Second Pass to set next and random pointers
        # cur = head
        # while cur:
        #     copy = oldToCopy[cur]
        #     copy.next = oldToCopy[cur.next]
        #     copy.random = oldToCopy[cur.random]
        #     cur = cur.next

        # return oldToCopy[head]    # Returning head from hashmap as it has already stored the mapping of original head to its corresponding copied node.     

        # 2. HashMap One Pass
        # oldToCopy = collections.defaultdict(lambda : Node(0)) # If key not present, it will create new node with default value 0
        # oldToCopy[None] = None # For handling edge case, random pointer pointing to null 

        # cur = head
        # while cur:
        #     oldToCopy[cur].val = cur.val # if key present, assign value from original list to node in hashmap else create new node 
        #     oldToCopy[cur].next = oldToCopy[cur.next]
        #     oldToCopy[cur].random = oldToCopy[cur.random]
        #     cur = cur.next
        # return oldToCopy[head]

        # Space Optimized - l1, l2 with pointer updations
        if not head:
            return None
        # Creating new list
        l1 = head
        while l1:
            l2 = Node(l1.val)
            l2.next = l1.random
            l1.random = l2
            l1 = l1.next
        # Setting newhead ref to start of newly created list l2
        newhead = head.random
        # Updating random pointers of l2
        l1 = head
        while l1:
            l2 = l1.random
            l2.random = l2.next.random if l2.next else None
            l1 = l1.next

        # Separating two lists
        l1 = head
        while l1 is not None:
            l2 = l1.random
            l1.random = l2.next
            l2.next = l1.next.random if l1.next else None
            l1 = l1.next

        return newhead


