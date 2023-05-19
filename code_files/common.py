from SortingTechniques_class import sorting_techniques
import time
import matplotlib.pyplot as plt
import random
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(10**6)
print(sys.getrecursionlimit())


def obtainedList(size):
    import random
    randomlist = []
    for i in range(0,size):
        n = random.randint(1,size)
        randomlist.append(n)

    return randomlist

def graph_func(timearr_average, input_sizes, title):
    plt.clf()
    plt.plot(timearr_average[0], label = "insertionSort",c='red')
    plt.plot(timearr_average[1], label = "mergeSort",c='green')
    plt.plot(timearr_average[2], label = "heapSort",c='blue')
    plt.plot(timearr_average[3], label = "quickSort",c='blue')
    plt.plot(timearr_average[4], label = "modifiedQuickSort",c='blue')
    plt.title(title)
    plt.xlabel('input sizes')
    plt.ylabel('average times')
    plt.legend()
    plt.show()
    plt.show()


def sortedList(sort_techniques, timearr_average, list_tobe_sorted, input_sizes):
    no_of_runs = 10
    timearr = [[] for i in range(len(input_sizes)*len(sort_techniques))]
    sortObject = sorting_techniques()
    for j in range(len(sort_techniques)):
        for k in range(no_of_runs):
            start = time.time()
            if sort_techniques[j] == "insertionSort":
                print("11111111")
                sorted_list = sortObject.insertionSort(list_tobe_sorted)
            elif sort_techniques[j] == "mergeSort":
                print("222222222")
                sorted_list = sortObject.mergeSort(list_tobe_sorted)
            elif sort_techniques[j] == "heapSort":
                print("333333333")
                sorted_list = sortObject.heapSort(list_tobe_sorted)
            elif sort_techniques[j] == "inplaceQuickSort":
                print("444444444")
                sorted_list = sortObject.quickSort(list_tobe_sorted, 0, len(list_tobe_sorted)-1)
            elif sort_techniques[j] == "ModifiedQuickSort":
                print("555555555")
                sorted_list = sortObject.modifiedQuickSort(list_tobe_sorted, 0, len(list_tobe_sorted)-1)
            end = time.time()
            timearr[j].append(end-start)
        print("timearr::",timearr)
        timearr_average[j].append(sum(timearr[j])/no_of_runs)
        print(timearr_average)
    return timearr_average


def main():
    
    sort_tech = ["insertionSort", "mergeSort", "heapSort", "inplaceQuickSort", "ModifiedQuickSort"]
    input_sizes = [1000]
    average_shuffle = [[] for i in range(len(input_sizes)*len(sort_tech))]
    average_sorted = [[] for i in range(len(input_sizes)*len(sort_tech))]
    average_reverse = [[] for i in range(len(input_sizes)*len(sort_tech))]

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
            
    graph_func(average_shuffle, input_sizes, "1. Sorting techniques for suffled list")
    graph_func(average_sorted, input_sizes, "2. Sorting techniques for sorted list")
    graph_func(average_reverse, input_sizes, "3. Sorting techniques for reverse list")
                
    

if __name__ == "__main__":
    main()
