"""Linked lists are lists that has each element store up the reference to its previous and next elements"""

'''Linked list element class'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.length = 1 if head else 0

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
        self.length += 1

    def get_position(self, pos):
        current = self.head
        counter = 1
        if self.head:
            while counter < pos:
                if current.next:
                    current = current.next
                    counter += 1
                else:
                    return None
            return current
        else:
            return None

    def insert(self, new_element, pos):
        current = self.head
        counter = 1
        prev = 0
        if self.head:
            while counter < pos:
                if current:
                    prev = current
                    current = current.next
                    counter += 1
                else:
                    return None
            new_element.next = current
            prev.next = new_element
            self.length += 1
        else:
            return None

    def replace(self, new_element, pos):
        current = self.head
        counter = 1
        if pos > 1:
            while counter < pos - 1:
                if current:
                    current = current.next
                    counter += 1
                else:
                    print("position out of list")
            new_element.next = current.next.next
            current.next = new_element
        else:
            new_element.next = current.next
            self.head = new_element

    def delete(self, value):
        current = self.head
        if self.head:
            if self.head.value == value:
                self.head = current.next
                self.length -= 1
            else:
                while current.next:
                    if current.next.value == value:
                        current.next = current.next.next
                        self.length -= 1
                        break
                    else:
                        current = current.next
        else:
            pass

    def get_middle(self):
        """
        1. get the pos of the middle element
        2. get the element in the middle position
        """
        mid_pos = (self.length // 2) + 1
        return self.get_position(mid_pos)

    def rotate_list(self, pos):
        """
        1. link the last element to the head
        2. break the element after the element at pos and make it the head
        """
        current = self.head
        counter = 1
        if self.head:
            while current.next:
                current = current.next
            current.next = self.head
            while counter <= pos:
                current = current.next
                counter += 1
            self.head = current.next
            current.next = None
        else:
            pass

    def display(self, label=""):
        current = self.head
        disp = str(current.value)
        while current.next:
            disp += " -> " + str(current.next.value)
            current = current.next
        disp += " -> Null"
        print(label, disp)

    def reverse(self):
        """
        1. use 3 pointers; head, temp1 and temp2
        2. the head holds the current node
        3. temp1 holds the previous node
        4. temp2 holds the next node
        """
        head = self.head
        prev_node = None
        while head:
            forward_node = head.next
            head.next = prev_node
            prev_node = head
            head = forward_node
        self.head = prev_node

    def get_value(self, node):
        return node.value if node else node

    def is_palindrome(self):
        """
        1. Uses 2 pointers, p1, p2
        2. p1 to track the end of the list, will move 2 steps per move
        3. p2 to get the middle of the list
        4. p2 will be used to break the list into 2 equal parts
        5. The second list will be reversed using the position of p2 as the initial head.
        6. The 2 list will be compared
        """
        p1 = p2 = self.head
        while self.head:
            p1 = p1.next.next
            p2 = p2.next
            if p1 == None:
                break
            if p1.next == None:
                p1 = p1.next
                #odd palindrome
                break
        print("p1:", self.get_value(p1), "p2:", self.get_value(p2))
        current = self.
        while p2:



e1 = Node(2)
e2 = Node(4)
e3 = Node(6)

e22 = Node(3)
e32 = Node(5)


linkedlist = LinkedList(e1)
linkedlist.append(e2)
linkedlist.append(e3)

linkedlist.display()

print("mid:", linkedlist.get_middle().value)

# insert
linkedlist.insert(e22, 2)
linkedlist.insert(e32, 4)

#
# # delete
linkedlist.delete(4)
linkedlist.delete(2)


linkedlist.display("list:")
linkedlist.rotate_list(2)
linkedlist.display("rotated at position 2:")
linkedlist.reverse()
linkedlist.display("reversed:")
linkedlist.replace(Node(6), 1)
linkedlist.display("replaced pos 1 element:")
linkedlist.is_palindrome()
