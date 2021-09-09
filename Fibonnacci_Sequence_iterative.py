def get_fib(position):
    first = 0
    second = 1
    next = first + second

    if position == 0 or position == 1:
        return position
    
    while (2 != position):
        position -= 1
        first = second
        second = next
        next = first + second
    return next

# Test cases
print(get_fib(9))
print(get_fib(10))
print(get_fib(0))