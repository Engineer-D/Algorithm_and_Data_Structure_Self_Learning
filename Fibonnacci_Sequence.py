"""
    Implement a function recursively to get the desired
    Fibonacci sequence value.
"""

def get_fib(position):
    if position == 0 or position == 1:
        return position
    return get_fib(position-1) + get_fib(position-2)

# Test cases
print(get_fib(9))
print(get_fib(10))
print(get_fib(0))