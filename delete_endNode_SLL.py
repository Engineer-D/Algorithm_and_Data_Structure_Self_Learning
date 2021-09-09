"""
    Tasks:
        Create a Node/Unit
        Create a linkedlist
        add to the linkedlist
        delete from the linked list
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
    
    #My Entry
    def delete(self):
        current = self.head
        while current.next:
            previous = current
            current = current.next
        del(current)
        previous.next = None
        return self.printlist()

    #Guide entry
    def deleteEnd(self):
        lastnode = self.head
        while lastnode.next is not None:
            previousNode = lastnode
            lastnode = lastnode.next
        previousNode.next = None


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
secondNode = Element(60)
thirdNode = Element(50)

linkedlist = LinkedList(head)
linkedlist.append(secondNode)
linkedlist.append(thirdNode)
linkedlist.printlist()
linkedlist.delete()