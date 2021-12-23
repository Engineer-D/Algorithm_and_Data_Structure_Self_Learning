from myStack import Stack

def infix2postfix(expression):
    prec = {} #The denote precedence
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack()
    postfix_list = []
    token_list = expression.split()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")" and not opStack.is_empty():
            topToken = opStack.pop()
            while topToken != "(":
                postfix_list.append(topToken)
                topToken = opStack.pop()
        elif token == ")" and  opStack.is_empty():
            return "Invalid Syntax"
        else:
            while (not opStack.is_empty()) and \
                (prec[opStack.peek()] >= prec[token]):
                postfix_list.append(opStack.pop())
            opStack.push(token)
    
    while not opStack.is_empty():
        postfix_list.append(opStack.pop())
    
    return " ".join(postfix_list)


print(infix2postfix(" A * B + ( ) ( ) C * D"))
print(infix2postfix("( A + B ) * C - ( D - E ) * ( F + G ) "))