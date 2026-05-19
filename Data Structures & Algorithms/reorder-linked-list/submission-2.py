# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        l1 = head
        # to find the mid of the linked list using fast and slow pointer
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #revierse the list after mid
        print(slow.val) 
        prev  = None
        curr = slow.next
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr
            curr = temp 
        l2 = prev
        idx = 1
        dummy = curr = l1
        l1 = l1.next
        while l1 and l2:
            if idx % 2 == 0:
                print('l1: ', l1.val)
                curr.next = l1
                l1 = l1.next
            else:
                print('l2: ', l2.val)
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            idx += 1
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        