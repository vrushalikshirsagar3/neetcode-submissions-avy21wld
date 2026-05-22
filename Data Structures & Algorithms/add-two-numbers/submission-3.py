# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        dummy = curr = ListNode(0)
        carry = 0
        while l1 and l2:
            new_node = ListNode(((l1.val + l2.val + carry) % 10) )
            curr.next = new_node
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
            curr = curr.next

        while l1:

            new_node = ListNode((l1.val  + carry) % 10)
            curr.next = new_node
            carry = (l1.val + carry) // 10
            l1 = l1.next
            curr = curr.next
        while l2:
            new_node = ListNode((l2.val + carry) % 10) 
            curr.next = new_node
            carry = (l2.val + carry) // 10
            l2 = l2.next
            curr = curr.next
        print(carry)
        if carry > 0:
            new_node = ListNode(carry)
            curr.next = new_node
        return dummy.next