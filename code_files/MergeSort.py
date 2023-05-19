
import time

def mergeSort(array):
    if (len(array) == 1):
        return array
    else:
        middle = len(array)//2
        leftArray = array[:middle]
        rightArray = array[middle:]
        leftArray = mergeSort(leftArray)
        rightArray = mergeSort(rightArray)
        return merge(leftArray, rightArray)

def generateList(size):
    import random
    random_list = []
    for i in range(0,size):
        n = random.randint(1,size)
        random_list.append(n)
    print(random_list)
    return random_list

def merge(leftArray, rightArray):
    resultArray = []
    while (len(leftArray)>0 and len(rightArray)>0):
        if (leftArray[0]>rightArray[0]):
            resultArray.append(rightArray[0])
            rightArray.remove(rightArray[0])
        else:
            resultArray.append(leftArray[0])
            leftArray.remove(leftArray[0])
    while (len(leftArray)>0):
        resultArray.append(leftArray[0])
        leftArray.remove(leftArray[0])
    while (len(rightArray)>0):
        resultArray.append(rightArray[0])
        rightArray.remove(rightArray[0])
    return resultArray



listSize = int(input("Enter the list size"))
list_to_sort = generateList(listSize)
print("Array before sorting:", list_to_sort)
begin = time.time()
list_to_sort = mergeSort(list_to_sort)
finish = time.time()
print("Array after Merge Sort:", list_to_sort)
print("The time of execution for merge sort is :", finish-begin)

