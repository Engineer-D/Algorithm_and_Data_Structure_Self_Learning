from myStack import Stack

def parCheck(symbolString):
    stack = Stack()
    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            stack.push(symbol)
            
        else:
            if stack.is_empty():
                balanced = False
            else:
                stack.pop()
        
        index += 1
    
    if balanced and stack.is_empty():
        return True
    else:
        return False

print(parCheck('((()))'))
print(parCheck('(()'))