'''
    Step:
        iterate through the array
        iterate through the index of the array
        check if the left is lesser than the right
        if True swap

        interesting thing is when iterating iterate in descending order
'''
def bubblesort(input_array):
    for i in range(len(input_array)-1, 0, -1):
        for j in range(i):
            if input_array[j] > input_array[j+1]:
                input_array[j],input_array[j+1] = input_array[j+1],input_array[j]

listArray = [2,53,6,34,4,6,2,8,12,17,45]
bubblesort(listArray)
print(listArray)