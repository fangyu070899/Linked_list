# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
            self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = None
        current = None

        while l1 != None or l2 != None:
            new_val = 0
            if l1 != None:
                new_val += l1.val
                l1 = l1.next
            if l2 != None:
                new_val += l2.val
                l2 = l2.next
            new_val += carry

            carry = new_val//10
            new_node = ListNode(val=new_val % 10)

            if head == None:
                head = new_node
                current = new_node
            else:
                current.next = new_node
                current = current.next
        if carry != 0:
            new_node = ListNode(val=carry)
            current.next = new_node
        return head
