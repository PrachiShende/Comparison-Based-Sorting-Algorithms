from SortingTechniques_class import sorting_techniques
import time
import matplotlib.pyplot as plt
import random
import numpy as np
import sys
print(sys.maxsize)
sys.setrecursionlimit(10**9)

def obtainedList(size):
    import random
    randomlist = []
    for i in range(0,size):
        n = random.randint(1,size)
        randomlist.append(n)
    return randomlist

def sortedList(sort_techniques, timearr_average, list_to_sort, input_sizes):
    runs = 20
    timeArray = [[] for i in range(len(input_sizes))]
    sortObject = sorting_techniques()
    for j in range(len(sort_techniques)):
        for k in range(runs):
            start = time.time()
            if j == 0:
                sorted_list = sortObject.insertionSort(list_to_sort)
            elif j == 1:
                sorted_list = sortObject.mergeSort(list_to_sort)
            elif j == 2:
                sorted_list = sortObject.heapSort(list_to_sort)
            elif j == 3:
                sorted_list = sortObject.quickSort(list_to_sort, 0, len(list_to_sort)-1)
            elif j == 4:
                sorted_list = sortObject.modifiedQuickSort(list_to_sort, 0, len(list_to_sort)-1)
            end = time.time()
            timeArray[j].append(end-start)
        timearr_average[j].append(sum(timeArray[j])/runs)
        timeArray[j]=[]
    return timearr_average

def graph_func(timearr_average, input_sizes, title):
    plt.plot(timearr_average[0], label = "insertionSort",c='red')
    plt.plot(timearr_average[1], label = "mergeSort",c='green')
    plt.plot(timearr_average[2], label = "heapSort",c='blue')
    plt.plot(timearr_average[3], label = "quickSort",c='yellow')
    plt.plot(timearr_average[4], label = "modifiedQuickSort",c='black')
    plt.title(title)
    plt.xlabel('input sizes')
    plt.ylabel('average times')
    plt.legend()
    plt.show()
    plt.show()




def main():
    
    sort_tech = ["insertionSort", "mergeSort", "heapSort", "quickSort", "modifiedQuickSort"]
    input_sizes = [1000, 2000, 4000, 5000, 10000, 20000, 40000, 50000, 60000, 80000, 100000]
    average_shuffle = [[] for i in range(len(input_sizes))]
    average_sorted = [[] for i in range(len(input_sizes))]
    average_reverse = [[] for i in range(len(input_sizes))]
    
    for i in range(len(input_sizes)):
        obtained_list = obtainedList(input_sizes[i])
        print("obtained_list",   obtained_list)

        shuffled_list = obtained_list
        random.shuffle(shuffled_list)

        print("shuffled_list::", shuffled_list)

        average_shuffle = sortedList(sort_tech, average_shuffle, shuffled_list, input_sizes)
        sorted_list = obtained_list
        sorted_list.sort()

        print("sorted_list::",sorted_list)

        average_sorted = sortedList(sort_tech, average_sorted, sorted_list, input_sizes)
        reversed_list = obtained_list
        reversed_list.sort(reverse=True)

        print("reversed_list::", reversed_list)

        average_reverse = sortedList(sort_tech, average_reverse, reversed_list, input_sizes)
            
    graph_func(average_shuffle, input_sizes, " 1 Sorting techniques for suffled list")
    graph_func(average_sorted, input_sizes, "2 Sorting techniques for sorted list")
    graph_func(average_reverse, input_sizes, "3 Sorting techniques for reverse list")
                
    

if __name__ == "__main__":
    main()
