# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 1. Brute Force
        # nodes = [] 
        # for lst in lists:  # Loop over every list in lists
        #     while lst:  # Loop over every number in single list item
        #         nodes.append(lst.val)  # Appendind values in node list
        #         lst = lst.next
        # nodes.sort()  # Sorting all the values taken from multiple lists

        # res = ListNode(0)  # Creating dummy node of linked list to start saving sorted list in LL
        # cur = res  # Using cur to iterate, res kept unchanged to keep track of start of the list
        # for node in nodes:
        #     cur.next = ListNode(node) # Creating node for every element/int
        #     cur = cur.next
        # return res.next  # Returning list from next of res, as it was a dummy node

        # 2. Merging Lists one by one
    #     if len(lists) == 0:  # Return none, if no items present in lists
    #         return None

    #     for i in range(1, len(lists)): # Loop starting from second list, so that it can be merged with i-1 i.e. first list
    #         lists[i] = self.mergeList(lists[i-1], lists[i]) # Calling merge function on first and second list
    #     return lists[-1]

    # def mergeList(self, l1, l2): # Function to merge two lists
    #     dummy = ListNode()
    #     tail = dummy

    #     while l1 and l2:
    #         if l1.val < l2.val:
    #             tail.next = l1
    #             l1 = l1.next
    #         else:
    #             tail.next = l2
    #             l2 = l2.next
    #         tail = tail.next
    #     if l1:
    #         tail.next = l1
    #     if l2:
    #         tail.next = l2
    #     return dummy.next

        # 3. Divide and Conquer (Iteration)
        # checking edge cases
    #     if not lists or len(lists) == 0:
    #         return None

    #     while len(lists) > 1: # Length should be more than 1, as we are merging two lists at a time
    #         mergedList = []
    #         for i in range(0, len(lists), 2): # Lopping through lists with increment of 2
    #             l1 = lists[i]
    #             l2 = lists[i+1] if (i+1) < len(lists) else None  # Checking if i is inbound
    #             mergedList.append(self.mergeLists(l1, l2))
    #         lists = mergedList  # lists will have -> All pairs of lists merged with sorted order
    #     return lists[0]

    # def mergeLists(self, l1: List[Optional[ListNode]], l2: List[Optional[ListNode]]):
    #     dummy = ListNode()
    #     cur = dummy
    #     while l1 and l2:
    #         if l1.val < l2.val:
    #             cur.next = l1
    #             l1 = l1.next
    #         else:
    #             cur.next = l2
    #             l2 = l2.next
    #         cur = cur.next
    #     if l1:
    #         cur.next = l1
    #     if l2:
    #         cur.next = l2
    #     return dummy.next
        
    # 4. Divide and conquer (Recursion)
        if not lists and len(lists) == 0:
            return None
        return self.divide(lists, 0, len(lists)-1)

    # Function to create halves of lists
    def divide(self, lists, l, r):
        # Checking base cases
        if l > r: # Invalid Range
            return None
        if l == r:
            return lists[l]
        mid = l + (r-l) // 2
        left = self.divide(lists, l, mid)
        right = self.divide(lists, mid+1, r)

        return self.conquer(left, right)

    # Function to merge left and right havles
    def conquer(self, l1, l2):
        dummy = ListNode()
        cur = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next



            