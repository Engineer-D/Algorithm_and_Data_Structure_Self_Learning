"""
    Steps: 
        Create Nodes
        Create Linked List
        Add Node to Linked List
        Print LinkedList
"""

# Creating Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Creating Linked List
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
    
    def printlist(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

#Node ==> data, next
firstNode = Node("David")
linkedlist = LinkedList()
linkedlist.append(firstNode)
secondNode = Node("Grandma")
linkedlist.append(secondNode)
linkedlist.printlist()