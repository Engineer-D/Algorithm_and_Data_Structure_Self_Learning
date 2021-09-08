"""
    task:
        create a unit
        create a linkedlist
        insert new node at the begining of linked list
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def prepend(self, newHead):
        currentHead = self.head
        if self.head:
            self.head = newHead
            self.head.next = currentHead
        else:
            self.head = newHead

    def printlist(self):
        if self.head is None:
            print("List is Empty")
            return
        current = self.head
        while current.next:
            print(current.data)
            current = current.next
        print(current.data)

#Node
node1 = Node(50)
node2 = Node(60)
node3 = Node(40)

linkedlist = LinkedList(node1)
linkedlist.append(node2)
linkedlist.prepend(node3)
linkedlist.printlist()