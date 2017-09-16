# 2.10 Insert a Node at the Front of a Linked List

class SinglyLinkedList:
    # constructor
    def __init__(self):
        self.head = None

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    # method for inserting a new node at the start of a Linked List
    def insert_at_front(self, data):
        node = Node()
        node.setData(data)
        node.setNext(self.head)

        self.setHead(node)

