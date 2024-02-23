# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        elif head.next == None:
            return head

        current = head
        head = current.next
        pre = None
        while True:
            if current == None or current.next == None:
                return head
            else:
                a = current
                b = current.next
                if pre != None:
                    pre.next = b
                a.next = b.next
                b.next = a
                pre = current
                current = a.next
