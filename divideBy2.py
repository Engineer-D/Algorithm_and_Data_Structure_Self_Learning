from myStack import Stack

def divide_by_2(number):
    stack = Stack()

    while number > 0:
        rem = number%2
        stack.push(rem)
        number = number//2
    
    binString = ""
    while not stack.is_empty():
        binString = binString + str(stack.pop())
    
    return binString

print(divide_by_2(1234567809876543234567898765432))