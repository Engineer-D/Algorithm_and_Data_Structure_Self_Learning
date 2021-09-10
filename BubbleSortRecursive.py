# Python Program for Implementation of Recursive Bubble Sort
class BubbleSort:
    """
        BubbleSort:
            function:
                BubbleSortRecursive: recursive function to sort array
                __str__ : format print of array
                __init__: constructor function in python
            variables:
                self.array = contains array
                self.length = length of array
    """

    def __init__(self, array):
        self.array = array
        self.length = len(array)
    
    def __str__(self):
        return " ".join([str(x) for x in self.array])

    def BubbleSortRecursive(self, n = None):
        if n is None:
            n = self.length
        
        #Base Case
        if n == 1:
            return
        
        # One Pass of bubble sort. After this pass, the largest element is moved
        # or  bubbled to end.
        for i in range(n - 1):
            if self.array[i] > self.array[i + 1]:
                self.array[i], self.array[i+1] = self.array[i+1], self.array[i]
        
        # Largest element is fixed recur for remaining array
        self.BubbleSortRecursive(n-1)

def main():
    listArray = [2,53,6,34,4,6,2,8,12,17,45]

    #Create object for class
    sort = BubbleSort(listArray)

    # Sorting array
    sort.BubbleSortRecursive()
    print("Sorted array: \n", sort) # This function/style is quite new and I like it

if __name__ == "__main__":
    main()