# 2.9 Inserting a Node at the End of a Singly Linked List

class SinglyLinkedList:
    # constructor
    def __init__(self):
        self.head = None

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    # method for inserting a new node at the end of a Linked List
    def insertAtEnd(self, data):
        new_node = Node()
        new_node.setData(data)

        if not self.head:
            self.head = new_node
        else:
            curr = self.head

            while curr.getNext():
                curr = curr.getNext()

            curr.setNext(new_node)

