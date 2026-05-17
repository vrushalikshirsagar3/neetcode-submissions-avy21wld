class ListNode:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node
class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        idx = 0
        while curr != None:
            if idx == index:
                return curr.val
            idx += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        if self.head == None:
            self.head = ListNode(val)
            self.head.next = None
            self.tail = self.head
        else:
            new_node = ListNode(val)
            new_node.next = self.head.next
            self.head.next = new_node
            if not new_node.next:
                self.tail = new_node
        curr = self.head
        while curr != None:
            print('after insert head', curr.val)
            curr = curr.next

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        curr = self.head 
        while curr != None:
            print(curr.val)
            curr = curr.next

    def remove(self, index: int) -> bool:
        idx = 0
        curr = self.head
        while idx < index and curr:
            idx += 1
            curr = curr.next
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            print('at index: ', idx, curr.val)
            return True
        return False

    def getValues(self) -> List[int]:
        curr = self.head.next
        listnodes = []
        while curr:
            listnodes.append(curr.val)
            print('get_values: ', curr.val)
            curr = curr.next
        return listnodes
