# Python program for implementation of Insertion Sort
import numpy as np

# Creating an array of integers with numpy
array = np.random.randint(-100, 100, 10)
arr_test = [63, 30, -57, -25, -41, 44, -88, 87, -95, -85]
arr_short = [7, 3, 4, 2, 5]


def selection_sort(arr):
    length = len(arr) - 1
    array_sorted = True

    # Print an array before sorting
    print('\n [-----------------BEFORE----------------]\n', arr, '\n')

    # Check if an array is sorted already
    for k in range(length):
        if arr[k] > arr[k + 1]:
            array_sorted = False

    # Insertion sort
    if not array_sorted:
        for i in range(1, len(arr)):
            key = arr[i]
            n = 1
            while key < arr[i - n] and i - n > -1:
                arr[i - n + 1] = arr[i - n]
                n += 1
            arr[i - n + 1] = key

            # Print an array after sorting
        print('\n [-----------------AFTER-----------------]\n', arr)
    else:
        # Print if an array does not need to be sorted
        print('\n Array is sorted already!')


if __name__ == '__main__':
    selection_sort(array)
