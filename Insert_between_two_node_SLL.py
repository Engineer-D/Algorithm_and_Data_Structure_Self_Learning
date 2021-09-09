"""
    task:
        create a unit
        create a linkedlist
        insert new node between two linked list
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # My Entry
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
            
    # Guide Entry
    def listlength(self):
        current = self.head
        length = 0
        while current is not None:
            length += 1
            current = current.next
        return length

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
            del currentHead
        else:
            self.head = newHead

    # My Entry
    def insert(self, newNode, position):
        counter = 0
        index = position
        current = self.head

        if position is 0:
            self.prepend(newNode)
            return
        elif position > self.nodelength() or position < 0:
            print("Out of Index")
            return
        else:
            while counter < index-1:
                current = current.next
                counter += 1
            nextNode = current.next
            current.next = newNode
            newNode.next = nextNode 
    
    # Guide Entry
    def insertat(self, newNode, position):
        currentNode = self.head
        currentPosition = 0

        if position is 0:
            self.prepend(newNode)
            return
        
        if position > self.listlength() or position < 0:
            print("Invalid position") 
            return

        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1


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
node4 = Node(45)
node5 = Node(55)

#linkedlist
linkedlist = LinkedList(node1)
linkedlist.append(node2)
linkedlist.prepend(node3)
linkedlist.insert(node4, 56)
linkedlist.insertat(node5, 40)
linkedlist.printlist()
#print(linkedlist.nodelength())