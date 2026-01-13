from .node import ListNode


class LinkedList:
    def __init__(self, head: ListNode):
        self.head = head

    def add(self, node: ListNode):
        placeholder = self.head
        while placeholder.next:
            placeholder = placeholder.next
        placeholder.next = node
