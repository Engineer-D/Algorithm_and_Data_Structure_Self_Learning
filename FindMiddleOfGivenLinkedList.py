"""
    Given a singly linked list, find the middle of the linked list. 
    For example, if the given linked list is 1->2->3->4->5 '
    then the output should be 3. 
    If there are even nodes, then there would be two middle nodes, 
    we need to print the second middle element. 
    For example, if given linked list is 1->2->3->4->5->6 
    then the output should be 4. 
"""

# Clreating Node Class
class Node():
    def __init__(self, value):
        self.value = value 
        self.next = None

# creating Linkedlist
class LinkedList():
    def __init__(self, head=None):
        self.head = head
        self.length = 0

    # Adding to the linkedlist at the end
    def append(self, newNode):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = newNode
            self.length += 1
        else:
            self.head = newNode
            self.length += 1

    # Adding to linkedList at the beginning
    def push(self, newNode):
        current = self.head
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    # getting the position of the a node in the linkedlist
    def findposition(self, position):
        if position < 0 and position > self.getLength():
            return None

        currentPos = 0
        current = self.head
        while current:
            if currentPos == position:
                return current.value
            else:
                currentPos += 1
                current = current.next
        return "Empty LinkedList, Try again"

    # printing items in a linked list
    def printList(self):
        current = self.head
        while current:
            print(current.value, "-->", end="")
            current = current.next
        print("Null")

    # Find the middle of the array
    def findMiddle(self):
        midIndex = self.length// 2
        return self.findposition(midIndex)
    
# Creating the empty linked list
ll = LinkedList()
l1 = Node(1) # creating first node
l2 = Node(2)
l3 = Node(3)
l4 = Node(4)
l5 = Node(5)
l6 = Node(6)

# Pushing
ll.push(l3) # pushing third node
ll.push(l2)
ll.push(l1)
# Appending 
ll.append(l4) # Appending fourth node
ll.append(l5)
ll.append(l6)

# Print all values in a linked list
ll.printList()

# Determine the middle of our linked list
print(ll.findMiddle())