"""
    Task:
        break the array into 1 piece
"""

def mergeSort(input_array):
    if len(input_array) <= 1:
        return input_array
    
    # find the midle point and divide it
    middle = len(input_array)//2
    leftList = input_array[:middle]
    rightList = input_array[middle:]

    leftList = mergeSort(leftList)
    rightList = mergeSort(rightList)
    return list(merge(leftList,rightList))

# Merge the sorted array
def merge(left, right):
    res = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            res.append(left[0])
            left.remove(left[0])
        else:
            res.append(right[0])
            right.remove(right[0])
    if len(left) == 0:
        res = res + right
    else:
        res = res + left
    return res

unsorted_list = [2,53,6,34,4,6,2,8,12,17,45]
print(mergeSort(unsorted_list))