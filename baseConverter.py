from myStack import Stack

def baseConverter(number, base):
    stack = Stack()

    digits = "0123456789ABCDEF"

    while number > 0:
        rem = number%base
        stack.push(rem)
        number = number//base
    
    numString = ""
    while not stack.is_empty():
        numString = numString + digits[stack.pop()]
    
    return numString

print(baseConverter(26, 26))