# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases
        dummy = ListNode()
        current = dummy

        # Traverse both lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach the remaining nodes (if any)
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # Return the merged list (skip dummy)
        return dummy.next

    # Helper function to convert list to linked list
    def to_linked_list(lst):
        dummy = ListNode()
        current = dummy
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    # Helper function to convert linked list to list
    def to_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result