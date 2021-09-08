"""
    Tasks:
        Create a Node/Unit
        Create a linkedlist
        add to the linkedlist
        delete from the linked list
        print out the linked list
"""

# Task 1: Create a Node
from typing import Counter


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

# Task 2: Create a linkedlist
class LinkedList(object):
    def __init__(self, head = None):
        self.head = head

    def nodelength(self):
        current = self.head
        length = 0
        if self.head:
            while current:
                length += 1
                current = current.next
            return length
        else:
            return length

    def isListEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    # adding to the linked list
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    #my Entry for delete head
    def deletehead(self):
        if self.head:
            current = self.head
            self.head = current.next
            del current
            return self.printlist()
        else:
            print("Linked list is empty, Delete action Failed!!")

    # guide entry
    def deleteHeadNode(self):
        if self.isListEmpty() is False:
            previousHead = self.head
            self.head = self.head.next
            previousHead.next = None
        else:
            print("Linked List if Empty, Delete Failed")

    #My Entry
    def deleteNode(self, position):
        if position < 0 or position >= self.nodelength():
            print("Invalid Index")
            return
        
        if self.isListEmpty() is False:
            if position is 0:
                self.deletehead()
                return
            current = self.head
            Counter = 0
            while self.head:
                if Counter < position:
                    Counter += 1
                    previous = current
                    current = current.next
                previous.next = current.next
                del current
                return self.printlist()

    #Guide entry
    def deletat(self, position):
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = currentNode.next
                currentNode.next = None
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1
        return self.printlist()


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
linkedlist.deleteNode(1)