"""
    Given a singly linked list, rotate the linked list counter-clockwise by k nodes. 
    Where k is a given positive integer. For example, if the given linked list is 
    10->20->30->40->50->60 and k is 4, 
    the list should be modified to 50->60->10->20->30->40. 
    Assume that k is smaller than the count of nodes in a linked list.
"""

# Creating a Node class
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

# Creating Linkedlist class
class LinkedList():
    def __init__(self, head=None):
        self.head = head
    
    # Adding to the Linkedlist at the end
    def append(self, newNode):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    # Getting total length of LinkedList
    def getLength(self):
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.next
        return counter

    # Print the values in the linkedlist
    def printList(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    
    # Point the lastNode to the head Node
    def mergeLastNodeAndHead(self):
        current = self.head
        while current.next:
            current = current.next
        current.next = self.head

    # Rotate the linkedlist 
    def rotateList(self, k):
        if k < 0 and k > self.getLength():
            return None
        
        current = self.head
        currentPos = 0
        previous = None
        self.mergeLastNodeAndHead()

        while current:
            if currentPos == k:
                previous.next = None
                self.head = current
                return self.head.value
            else:
                currentPos += 1
                previous = current
                current = current.next

                

# Creating Node              
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)
node6 = Node(60)

# Creating LinkedList
ll = LinkedList(node1)
ll.append(node2)
ll.append(node3)
ll.append(node4)
ll.append(node5)
ll.append(node6)

# Perform the Operation
ll.rotateList(4)
ll.printList()