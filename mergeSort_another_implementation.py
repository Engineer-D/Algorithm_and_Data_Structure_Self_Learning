"""
    Task:
        break the array into 1 piece
        sort it pair by pair
        continue the chain till you get the full array back
"""
from mergeSort import merge


def mergeSort(array):
    if len(array) > 1:
        
        # findding the mid of the array
        mid = len(array)//2

        # dividing the array elements
        left = array[:mid]
        right = array[mid:]

        #sorting the left half
        mergeSort(left)

        #sorting the right half
        mergeSort(right)

        i = j = k = 0

        # Copy data to temp arrays left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        
        # Checking if any element was left
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j+=1
            k+=1

# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end = " ")
    print()

# Driver Code
if __name__ == '__main__':
    array = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    print("Given array is", end="\n")
    printList(array)
    mergeSort(array)
    print("Sorted array is: ", end='\n')
    printList(array)