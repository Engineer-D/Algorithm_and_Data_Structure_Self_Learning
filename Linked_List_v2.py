"""
    Tasks:
        Create a Node/Unit
        Create a linkedlist
        add to the linkedlist
        print out the linked list
"""

# Task 1: Create a Node
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

# Task 2: Create a linkedlist
class LinkedList(object):
    def __init__(self, head = None):
        self.head = head

    # adding to the linked list
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
    
    def printlist(self):
        if self.head is None:
            print("List is Empty")
            return
        current = self.head
        while current.next:
            print(current.value)
            current = current.next
        print(current.value)

# Creating the head node
head = Element(40)
linkedlist = LinkedList(head)
secondNode = Element(60)
linkedlist.append(secondNode)
thirdNode = Element(50)
linkedlist.append(thirdNode)
linkedlist.printlist()