# Python program for implementation of Bubble Sort
import numpy as np

# Creating an array of integers with numpy
array = np.random.randint(-100, 100, 10)


def bubble_sort(arr):
    length = len(arr) - 1
    array_sorted = True

    # Print an array before sorting
    print('\n [-----------------BEFORE----------------]\n', arr, '\n')

    # Check if an array is sorted already
    for k in range(length):
        if arr[k] > arr[k + 1]:
            array_sorted = False

    # Sorting an array by swapping adjacent elements
    if not array_sorted:
        for n in range(length):
            for i in range(length - n):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
        # Print an array after sorting
        print('\n [-----------------AFTER-----------------]\n', arr)
    else:
        # Print if an array does not need to be sorted
        print('\n Array is sorted already!')


if __name__ == '__main__':
    bubble_sort(array)
