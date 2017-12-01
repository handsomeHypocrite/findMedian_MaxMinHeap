#Bokai Chen
#The program uses MAX MIN heap to find the median of the array.
#additional number can be added repetitively after initial array is created
#input format is 1,2,3,4
#note: if size of input is even, the middle 2 numbers are averaged

import heapq
import numpy as np
import statistics


def randarr():
    """generating random test data"""
    randArr = np.random.rand(int(10 * np.random.rand(1)))
    return [int(100 * i) for i in randArr]


def inputArr():
    """Getting user input and convert into int list"""
    rawInput = input("please enter initial/additional array, eg: 1,2,3 \n")
    if len(rawInput) > 0:
        Array = [int(num) for num in rawInput.split(",")]
    else:
        Array = []
    return Array


def arrInsertHeap(array, RoR):
    """Inserting new integers into heaps"""
    global left_heap, right_heap
    for num in array:
#RoR is the root of the right heap, this is to ensure all elements in the left heap is smaller than all elements int the right heap
        if num < RoR:
            heapq.heappush(left_heap, -num)
        else:
            heapq.heappush(right_heap, num)

# Blancing the size of the 2 heaps
    adjustment = len(left_heap) - len(right_heap)

    if adjustment > 0:
        for i in range(int(adjustment / 2)):
            heapq.heappush(right_heap, -heapq.heappop(left_heap))
    elif adjustment < 0:
        for i in range(int(-adjustment / 2)):
            heapq.heappush(left_heap, -heapq.heappop(right_heap))

# Extracting median from the heaps
def medFromHeap():
    global left_heap, right_heap
    if len(left_heap) - len(right_heap) == 0:
        median = (-left_heap[0] + right_heap[0]) / 2
    elif len(right_heap) > len(left_heap):
        median = right_heap[0]
    else:
        median = -left_heap[0]

    return median



#initialization
array = []
left_heap = []
right_heap = []
RoR = 0

while True:

    newNumbers = inputArr()

#to test with random numbers, uncomment
    # newNumbers = randarr()
    # array += newNumbers

    if len(right_heap)>0:
        RoR = right_heap[0]


    arrInsertHeap(newNumbers, RoR)

    median = medFromHeap()

    print("calcuated median: %.1f" %median)

#Check result using statistics module, uncomment
    # realMed = statistics.median(array)
    # print("actual median: %.1f" %realMed)

    print("\n")
