import time

def insersionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while (j >= 0 and key < array[j]):
            temp = array[j]
            array[j] = key
            array[j+1] = temp
            j = j - 1
    
def obtainedList(size):
    import random
    random_list = []
    for i in range(0,size):
        n = random.randint(1,size)
        random_list.append(n)
    print(random_list)
    return random_list

listSize = 100000
list_to_sort = obtainedList(listSize)
print("Array before sorting:", list_to_sort)
begin = time.time()
insersionSort(list_to_sort)
finish = time.time()
print("Array after Insersion Sort:", list_to_sort)
print("The time of execution of insertion sort is :", finish-begin)


