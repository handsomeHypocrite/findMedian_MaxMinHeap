#Bokai Chen
#The program uses MAX MIN heap to find the median of the array.
#additional number can be added after initial array is created

import heapq
import numpy as np
import statistics

# rawInput2 = input("please enter additional array \n")

def randarr():
    randArr = np.random.rand(int(10 * np.random.rand(1)))
    return [int(100 * i) for i in randArr]


def inputArr():
    rawInput = input("please enter initial/additional array, eg: 1,2,3 \n")
    if len(rawInput) > 0:
        Array = [int(num) for num in rawInput.split(",")]
    else:
        Array = []
    return Array


def arrInsertHeap(array, RoR):
    global left_heap, right_heap
    for num in array:
        if num < RoR:
            heapq.heappush(left_heap, -num)
        else:
            heapq.heappush(right_heap, num)

    # print(left_heap)
    # print(right_heap)
    # print(len(left_heap))
    # print(len(right_heap))


    adjustment = len(left_heap) - len(right_heap)

    # print(adjustment)

    if adjustment > 0:
        for i in range(int(adjustment / 2)):
            heapq.heappush(right_heap, -heapq.heappop(left_heap))
    elif adjustment < 0:
        for i in range(int(-adjustment / 2)):
            heapq.heappush(left_heap, -heapq.heappop(right_heap))

    # print(left_heap)
    # print(right_heap)
    # print(len(left_heap))
    # print(len(right_heap))

def medFromHeap():
    global left_heap, right_heap
    if len(left_heap) - len(right_heap) == 0:
        median = (-left_heap[0] + right_heap[0]) / 2
        print("both heap used")
    elif len(right_heap) > len(left_heap):
        median = right_heap[0]
        print("right heap used")
    else:
        median = -left_heap[0]
        print("left heap used")

    return median


array = []
left_heap = []
right_heap = []
RoR = 0

while True:

    newNumbers = inputArr()
    newNumbers = randarr()
    array += newNumbers

    if len(right_heap)>0:
        RoR = right_heap[0]


    arrInsertHeap(newNumbers, RoR)

    median = medFromHeap()

    print("length of array is: %d" %len(array))
    print("length of left heap is: %d" %len(left_heap))
    print("length of right heap is: %d" %len(right_heap))

    print(array)
    print(left_heap)
    print(right_heap)

    realMed = statistics.median(array)


    print("calcuated median: %d" %median)
    print("actual median: %d" %realMed)
    print("\n")
