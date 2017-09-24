# 2.2 Reverse a Singly Linked List

class SinglyLinkedList:
    # constructor
    def __init__(self):
        self.head = None

    # method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head

    def reverse(self):
        curr = self.head
        last = None

        while curr:
            temp_next = curr.next
            curr.next = last
            last = curr
            curr = temp_next

        self.head = last
