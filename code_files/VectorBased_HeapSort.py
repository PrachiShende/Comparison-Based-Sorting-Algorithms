import time

def heapSort(array):
    n = len(array)
    for i in range(n // 2 -1, -1, -1):
        heapify(array, n, i)

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

    return array

def heapify(array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if ((left < n) and (array[i] < array[left])):
        largest = left

    if ((right < n) and (array[largest] < array[right])):
        largest = right

    if (largest != i):
        array[i],array[largest] = array[largest],array[i] 
        heapify(array, n, largest)

def obtainedList(size):
    import random
    randomlist = []
    for i in range(1,size+1):
        n = random.randint(1,size)
        randomlist.append(n)

    return randomlist

listSize = 10000
list_to_sort = obtainedList(listSize)
print("Array before sorting:", list_to_sort)
start = time.time()
list_to_sort = heapSort(list_to_sort)
end = time.time()
print("The time of execution of heapsort is :", end-start)
print("Array after heap sort Sort:", list_to_sort)
