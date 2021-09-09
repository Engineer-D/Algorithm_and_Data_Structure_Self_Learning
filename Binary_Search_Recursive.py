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
def BinarySearchRec(input_array, value, left, right):
    #check base case
    if right >= left:
        mid = (right+left)//2

        # If Element is present at the middle itself
        if input_array[mid] == value:
            return mid
        #if element is smaller than mid, then it's present
        #in the left subarray
        elif input_array[mid] > value:
            right = mid -1
            return BinarySearchRec(input_array, value, left, right)
        else:
            left = mid + 1
            return BinarySearchRec(input_array, value, left, right)

    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15

right = len(test_list) - 1
print(BinarySearchRec(test_list, test_val1, 0, right))
print(BinarySearchRec(test_list, test_val2, 0, right))