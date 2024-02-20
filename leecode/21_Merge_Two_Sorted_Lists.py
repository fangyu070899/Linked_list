# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        current = None
        while list1 != None or list2 != None:
            pick = None
            if list1 == None:
                pick = list2
                list2 = list2.next
            elif list2 == None:
                pick = list1
                list1 = list1.next
            elif list1.val <= list2.val:
                pick = list1
                list1 = list1.next
            elif list1.val > list2.val:
                pick = list2
                list2 = list2.next

            if head == None:
                head = pick
                current = pick
            else:
                current.next = pick
                current = current.next
        return head
