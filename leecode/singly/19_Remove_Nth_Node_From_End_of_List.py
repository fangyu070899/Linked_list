# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def len(self, head):
        current = head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        index = self.len(head) - n
        if index == 0:
            if head.next != None:
                head = head.next
            else:
                head = None
            return head

        current = head
        prev = head
        position = 0
        while current != None and position != index:
            prev = current
            current = current.next
            position += 1

        if current != None:
            prev.next = current.next

        return head
