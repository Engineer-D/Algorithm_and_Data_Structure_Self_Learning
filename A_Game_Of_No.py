# Creating Node Class
class Node():
    def __init__(self, value):
        self.value = value 
        self.next = None

# creating Linkedlist
class LinkedList():
    def __init__(self, head=None):
        self.head = head
        self.length = 0

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

    # main function
    def GameOfNo(self):
        N = self.length-1
        result = LinkedList()
        status = True
        for i in range(N):
            q = i+1
            while q <= N:
                if self.findposition(i) < self.findposition(q):
                    r = q+1
                    while r <= N:
                        if self.findposition(q) > self.findposition(r):
                            status = False
                            result.push(Node(self.findposition(r)))
                            break
                        else:
                            r += 1
                    break
                else:
                    q += 1
                    status = True
            if status:
                result.push(Node(-1))
        result.push(Node(-1))
        result.reverse()
        print(result.printList())
    
# Creating the empty linked list
ll = LinkedList()
l1 = Node(2) # creating first node
l2 = Node(5)
l3 = Node(4)
l4 = Node(8)
l5 = Node(7)
l6 = Node(1)
l7 = Node(7)
l8 = Node(3)

# Pushing
ll.push(l1)
ll.push(l2)
ll.push(l3)
ll.push(l4)
ll.push(l5)
ll.push(l6)
ll.push(l7)
ll.push(l8)

# Print all values in a linked list
ll.printList()

# Determine the middle of our linked list
ll.GameOfNo()