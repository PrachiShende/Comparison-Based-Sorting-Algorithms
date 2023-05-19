#import sys
#sys.setrecursionlimit(10**8)
import random
class sorting_techniques:
    
    """Insertion Sort"""
    def insertionSort(self, array):
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while (j >= 0 and key < array[j]):
                temp = array[j]
                array[j] = key
                array[j+1] = temp
                j = j - 1
        return array

    """Merge Sort"""
    def mergeSort(self, array):
        if (len(array) == 1):
            return array
        else:
            mid = len(array)//2
            left_arr = array[:mid]
            right_arr = array[mid:]
            left_arr = self.mergeSort(left_arr)
            right_arr = self.mergeSort(right_arr)
            return self.merge(left_arr, right_arr)

    def merge(self, left_arr, right_arr):
        final_arr = []
        while (len(left_arr)>0 and len(right_arr)>0):
            if (left_arr[0]>right_arr[0]):
                final_arr.append(right_arr[0])
                right_arr.remove(right_arr[0])
            else:
                final_arr.append(left_arr[0])
                left_arr.remove(left_arr[0])
        while (len(left_arr)>0):
            final_arr.append(left_arr[0])
            left_arr.remove(left_arr[0])
        while (len(right_arr)>0):
            final_arr.append(right_arr[0])
            right_arr.remove(right_arr[0])
        return final_arr


    """Vector Based Heap sort"""
    def heapSort(self, array):
        n = len(array)
        for i in range(n // 2 -1, -1, -1):
            self.heapify(array, n, i)
        for i in range(n-1, 0, -1):
            array[i], array[0] = array[0], array[i]
            self.heapify(array, i, 0)
        return array

    def heapify(self, array, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if ((left < n) and (array[i] < array[left])):
            largest = left
        if ((right < n) and (array[largest] < array[right])):
            largest = right
        if (largest != i):
            array[i],array[largest] = array[largest],array[i]   #sort
            self.heapify(array, n, largest)

    """Modified Quick Sort - Median of three as pivot"""
    def median(self, arr, start, end):
        middle = (start + end)//2
        if arr[middle] < arr[start]:
            temp = arr[start]
            arr[start] = arr[middle]
            arr[middle] = temp
        if arr[end] < arr[start]:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
        if arr[end] < arr[middle]:
            temp = arr[middle]
            arr[middle] = arr[end]
            arr[end] = temp
        temp = arr[middle]
        arr[middle] = arr[end-1]
        arr[end-1] = temp
        return arr[end-1]

    def modifiedQuickSort(self, arr, start, end):
        if(start + 10 < end):
            pivot = self.median(arr, start, end)
            i = start
            j = end - 1
            sorted1 = True
            while sorted1:
                while (arr[i] < pivot):
                    i = i + 1
                while (pivot < arr[j]):
                    j = j - 1
                    arr[i], arr[j] = arr[j], arr[i]
                    sorted1 = False
                else:
                    sorted1 = False
            temp = arr[i]
            arr[i] = arr[end - 1]
            arr[end - 1] = temp
            self.modifiedQuickSort(arr, start, i-1)
            self.modifiedQuickSort(arr, i+1, end)
        else:
            self.insertionSort(arr)

    def quickSort(self, arr, start , end):
        if(start < end):
            pivotindex = self.partitionRand(arr,start, end)
            self.quickSort(arr , start , pivotindex-1)
            self.quickSort(arr, pivotindex + 1, end)
 
    def partitionRand(self, arr , start, end):
        randpivot = random.randrange(start, end)
        arr[start], arr[randpivot] =arr[randpivot], arr[start]
        return self.partition(arr, start, end)
 

    def partition(self, arr,start,end):
        pivot = start
        i = start + 1
        for j in range(start + 1, end + 1):
            if arr[j] <= arr[pivot]:
                arr[i] , arr[j] = arr[j] , arr[i]
                i = i + 1
        arr[pivot] , arr[i - 1] =arr[i - 1] , arr[pivot]
        pivot = i - 1
        return (pivot)
    




    

    
