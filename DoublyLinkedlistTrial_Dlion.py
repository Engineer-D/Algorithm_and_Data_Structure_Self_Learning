import time
start = time.time()

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
        
    def __len__(self):
        return self.size

    def PrintList(self):
        current=self.head
       
        while current is not None:
            print(current.data, '-->', end="")
            current=current.next
        print('NULL')
            
            
    def append(self, newdata):
        newNode=Node(newdata)
        current=self.head
        last=self.tail
        if self.head and self.tail:
            while current.next and last.prev:
                current=current.next
                last=last.prev
            current.next=newNode
            last= newNode
            last.prev=current
            self.tail=last
            self.size+=1
        else:
            self.head=newNode
            self.tail=newNode
            self.size+=1
            
    def ispalindrome(self):
        last=self.tail
        current=self.head
        palindrome_count=1
        if self.head and self.tail:
            while current.next and last.prev:
                if current.data==last.data:
                    current=current.next
                    last=last.prev
                    palindrome_count+=1
                else:
                    break
                
        if palindrome_count==self.size:
            return True
        else:
            return False

    def opt_palindrome(self):
        midPos=self.size//2
        last=self.tail
        current=self.head
        palindrome_count=0

        if self.head and self.tail:
            while current.next and last.prev and palindrome_count < midPos:
                if current.data==last.data:
                    current=current.next
                    last=last.prev
                    palindrome_count+=1
                else:
                    return False
            
        return True


s=LinkedList()
s.append('h')
s.append('a')
s.append('n')
s.append('n')
s.append('a')
s.append('h')


s.PrintList()
print(s.opt_palindrome())

print("---------------%s SecondsI--------------------"%(time.time() - start))
