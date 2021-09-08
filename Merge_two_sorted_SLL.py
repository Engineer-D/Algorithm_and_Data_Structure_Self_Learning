"""
    steps:
        create a unit
        create a linked list
        add to your linked list
        compare the head of the first LL with Second
        use least as head and compare other nodes and get the sorted list
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
    
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def printlist(self):
        current = self.head
        if current:
            while current:
                print(current.value)
                current = current.next
        else:
            print('Empty Linked List')

# Nodes
L1_node1 = Node(1)
L1_node2 = Node(3)
L1_node3 = Node(4)

L2_node1 = Node(2)
L2_node2 = Node(7)
L2_node3 = Node(9)

#Linked List
linkedlist1 = LinkedList(L1_node1)
linkedlist1.append(L1_node2)
linkedlist1.append(L1_node3)

linkedlist2 = LinkedList(L2_node1)
linkedlist2.append(L2_node2)
linkedlist2.append(L2_node3)

linkedlist1.printlist()
linkedlist2.printlist()