import time

def modifiedQuickSort(array, begin, finish):
    if(begin < finish):
        center = median(array, begin, finish)
        i = begin
        j = finish - 1
        sorted = True
        while sorted:
            while (array[i] < center):
                i = i + 1
            while (center < array[j]):
                j = j - 1
            if(i < j):
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
            else:
                sorted = False
        temp = array[i]
        array[i] = array[finish - 1]
        array[finish - 1] = temp
        modifiedQuickSort(array, begin, i-1)
        modifiedQuickSort(array, i+1, finish)
    else:
        insersionSort(array)


def median(array, begin, finish):
    middle = (begin + finish)//2
    if array[middle] < array[begin]:
        temp = array[begin]
        array[begin] = array[middle]
        array[middle] = temp
    if array[finish] < array[begin]:
        temp = array[begin]
        array[begin] = array[finish]
        array[finish] = temp
    if array[finish] < array[middle]:
        temp = array[middle]
        array[middle] = array[finish]
        array[finish] = temp
    temp = array[middle]
    array[middle] = array[finish-1]
    array[finish-1] = temp
    return array[finish-1]

def generateList(size):
    import random
    randomlist = []
    for i in range(0,size):
        n = random.randint(1,size)
        randomlist.append(n)
    print("The default array: ",randomlist)
    return randomlist

                
def insersionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while (j >= 0 and key < array[j]):
            temp = array[j]
            array[j] = key
            array[j+1] = temp
            j = j - 1

arraySize = 100
array = generateList(arraySize)
begin = time.time()
sortedArray = modifiedQuickSort(array, 0, arraySize-1)
finish = time.time()
print("The sorted array: ", sortedArray)
print("The time complexity is: ", finish-begin)
