# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        hade = None
        node = None
        
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        while True:
            if list1 is None:
                node.next = list2
                break
            if list2 is None:
                node.next = list1
                break
            smaller_node = list1
            if list2.val < smaller_node.val:
                smaller_node = list2
                list2 = list2.next
            else:
                list1 = list1.next
                
            if head is None:
                head = smaller_node
            if node is None:
                node = smaller_node
            else:
                node.next = smaller_node
                node = node.next
                
        return head
        