from myStack import Stack

def symCheck(symbolString):
    stack = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            stack.push(symbol)
        else:
            if stack.is_empty():
                balanced = False
            else:
                top = stack.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1
    
    if balanced and stack.is_empty():
        return True
    else:
        return False

def matches(open, close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)

print(symCheck('{{([][])}()}'))
print(symCheck('[{()]'))