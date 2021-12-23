"""
    Given pointer to the head node of a linked list, the task is to reverse the linked list. 
    We need to reverse the list by changing the links between nodes.

    Input: Head of following linked list 
    1->2->3->4->NULL 
    Output: Linked list should be changed to, 
    4->3->2->1->NULL
"""

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class linkedList():
    def __init__(self, head=None):
        self.head = head

    # Add Node to linkedlist
    def append(self, newNumber):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = newNumber
        else:
            self.head = newNumber
    
    # Print the values in the linkedlist
    def printList(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def reverse(self):
        previous = None
        current = self.head
        nextLink = None
        
        while current:
            nextLink = current.next 
            current.next = previous
            previous = current
            current = nextLink
        self.head = previous


# Creating Node              
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

# Creating LinkedList
ll = linkedList(node1)
ll.append(node2)
ll.append(node3)
ll.append(node4)
ll.append(node5)
ll.append(node6)

# Perform the Operation
ll.reverse()
ll.printList()