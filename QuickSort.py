def quicksort(array):
    elements = len(array)

    # Base Case
    if elements < 2:
        return array

    currentPos = 0 #Position of the partitioning element
    for i in range(1, elements):
        if array[i] <= array[0]:
            currentPos += 1
            temp = array[i]
            array[i] = array[currentPos]
            array[currentPos] = temp
    
    temp = array[0]
    array[0] = array[currentPos]
    array[currentPos] = temp # Brings pivot to it's appropriate position

    left = quicksort(array[0:currentPos])
    right = quicksort(array[currentPos+1:elements])

    array = left + [array[currentPos]] + right # Merging everything together

    return array

unsorted_list = [2,53,6,34,4,6,2,8,12,17,45]
print(quicksort(unsorted_list))