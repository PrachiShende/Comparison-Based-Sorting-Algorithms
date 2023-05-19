
import random
class sorting_techniques:
    
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

    def mergeSort(self, array):
        if (len(array) == 1):
            return array
        else:
            middle = len(array)//2
            left_array = array[:middle]
            right_array = array[middle:]
            left_array = self.mergeSort(left_array)
            right_array = self.mergeSort(right_array)
            return self.merge(left_array, right_array)

    def merge(self, left_array, right_array):
        resulted_array = []
        while (len(left_array)>0 and len(right_array)>0):
            if (left_array[0]>right_array[0]):
                resulted_array.append(right_array[0])
                right_array.remove(right_array[0])
            else:
                resulted_array.append(left_array[0])
                left_array.remove(left_array[0])
        while (len(left_array)>0):
            resulted_array.append(left_array[0])
            left_array.remove(left_array[0])
        while (len(right_array)>0):
            resulted_array.append(right_array[0])
            right_array.remove(right_array[0])
        return resulted_array

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
        left = 2*(i + 1)
        right = 2*(i + 2)
        if ((left < n) and (array[i] < array[left])):
            largest = left
        if ((right < n) and (array[largest] < array[right])):
            largest = right
        if (largest != i):
            array[i],array[largest] = array[largest],array[i]   #sort
            self.heapify(array, n, largest)

    def median(self, array, start, finish):
        middle = (start + finish)//2
        if array[middle] < array[start]:
            temp = array[start]
            array[start] = array[middle]
            array[middle] = temp
        if array[finish] < array[start]:
            temp = array[start]
            array[start] = array[finish]
            array[finish] = temp
        if array[finish] < array[middle]:
            temp = array[middle]
            array[middle] = array[finish]
            array[finish] = temp
        temp = array[middle]
        array[middle] = array[finish-1]
        array[finish-1] = temp
        return array[finish-1]

    def modifiedQuickSort(self, array, start, finish):
        if(start + 10 < finish):
            center = self.median(array, start, finish)
            i = start
            j = finish - 1
            sorted1 = True
            while sorted1:
                while (array[i] < center):
                    i = i + 1
                while (center < array[j]):
                    j = j - 1
                    array[i], array[j] = array[j], array[i]
                    sorted1 = False
                else:
                    sorted1 = False
            temp = array[i]
            array[i] = array[finish - 1]
            array[finish - 1] = temp
            self.modifiedQuickSort(array, start, i-1)
            self.modifiedQuickSort(array, i+1, finish)
        else:
            self.insertionSort(array)

    def quickSort(self, array, start , finish):
        if(start < finish):
            pivotindex = self.partitionRand(array,start, finish)
            self.quickSort(array , start , pivotindex-1)
            self.quickSort(array, pivotindex + 1, finish)
 
    def partitionRand(self, array , start, finish):
        random_pivot = random.randrange(start, finish)
        array[start], array[random_pivot] =array[random_pivot], array[start]
        return self.partition(array, start, finish)
 

    def partition(self, array,start,finish):
        center = start
        i = start + 1
        for j in range(start + 1, finish + 1):
            if array[j] <= array[center]:
                array[i] , array[j] = array[j] , array[i]
                i = i + 1
        array[center] , array[i - 1] =array[i - 1] , array[center]
        center = i - 1
        return (center)
    




    

    
