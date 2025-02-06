# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # # Defining new node 
        # dummy = result = ListNode()

        # # Loop to traverse all nodes in both lists
        # while list1 and list2:
        #     if list1.val < list2.val:
        #         result.next = list1
        #         list1 = list1.next
        #     else:
        #         result.next = list2
        #         list2 = list2.next
        #     result = result.next

        # # Appending remaining list if one of them is empty
        # result.next = list1 or list2

        # return dummy.next

        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2   
