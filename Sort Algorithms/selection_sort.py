# Python program for implementation of Bubble Sort
import numpy as np

# Creating an array of integers with numpy
array = np.random.randint(-100, 100, 10)
arr_test = [63, 30, -57, -25, -41, 44, -88, 87, -95, -85]


def selection_sort(arr):
    length = len(arr)-1
    array_sorted = True

    # Print an array before sorting
    print('\n [-----------------BEFORE----------------]\n', arr, '\n')

    # Check if an array is sorted already
    for k in range(length):
        if arr[k] > arr[k + 1]:
            array_sorted = False

    # Selection sort
    # arr[min_index] -> minimum value
    if not array_sorted:
        for n in range(length):
            min_index = n
            for i in range(n, length+1):
                if arr[min_index] > arr[i]:
                    min_index = i
            arr[n], arr[min_index] = arr[min_index], arr[n]

        # Print an array after sorting
        print('\n [-----------------AFTER-----------------]\n', arr)
    else:
        # Print if an array does not need to be sorted
        print('\n Array is sorted already!')


if __name__ == '__main__':
    selection_sort(array)
