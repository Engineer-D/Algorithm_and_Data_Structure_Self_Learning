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

def mergesorted(l1, l2, m):
    current1 = l1.head
    current2 = l2.head
    merger = m

    while True:
        if current1 is None:
            merger.append(current2)
            break

        if current2 is None:
            merger.append(current1)
            break

        if current1.value < current2.value:
            current1Next = current1.next
            current1.next =  None
            merger.append(current1)
            current1 = current1Next
        else:
            current2Next = current2.next
            current2.next = None
            merger.append(current2)
            current2 = current2Next
    
    return m.printlist() 

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

mergerlist = LinkedList()

mergesorted(linkedlist1, linkedlist2, mergerlist)