import numpy as np
import time
import sys
sys.setrecursionlimit(5000)


def divide(array, begin, finish):
    i = (begin - 1)
    center = array[finish]
    for j in range(begin, finish):
        if array[j] <= center:
            i = i+1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
    temp = array[i+1]
    array[i+1] = array[finish]
    array[finish] = temp
    return (i+1)

def quickSort(array, begin, finish):
    if len(array) == 1:
        return array
    if begin < finish:
        partition_index = divide(array, begin, finish)
        quickSort(array, begin, partition_index - 1)
        quickSort(array, partition_index + 1, finish)
        return array

size_of_array = 10000
unsorted_array = np.random.randint(1,10,size_of_array)
print("Default Array: ", unsorted_array)
beginTime = time.time()
sorted_array = quickSort(unsorted_array, 0, size_of_array-1)
print("The sorted array is: ", sorted_array)
finishTime = time.time()
print("The time complexity is: ", finishTime-beginTime)

