"""
    Task:
        Implement Binary serch using iterative method
        Logic*
            - Set Low
            - Set High
            - Calc mid
            - Write conditions to check for the data we are serching for
        Understand that binary search returns the index of that data/value you are looking for
        works more like index() function in python
        return -1 if the value is not in the array
"""

### Implementation

def BinarySearch(input_array, value):
    left = 0
    right = len(input_array) - 1

    while (left <= right):
        mid = int(left + ((right - left)/2))
        if input_array[mid] == value:
            return mid
        elif input_array[mid] < value:
            left = mid + 1
        else:
            right = mid -1
    else:
        return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(BinarySearch(test_list, test_val1))
print(BinarySearch(test_list, test_val2))