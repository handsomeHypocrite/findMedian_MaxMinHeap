#Bokai Chen
#The program uses MAX MIN heap to find the median of the array.
#additional number can be added after initial array is created

import heapq
import numpy as np
import statistics

rawInput = input("please enter initial array, eg: 1,2,3 \n")
rawInput2 = input("please enter additional array \n")


randArr = np.random.rand(int(100*np.random.rand(1)))
arr = [int(100*i) for i in randArr]


if len(rawInput) > 0:
    initialArray = [int(num) for num in rawInput.split(",")]
else:
    initialArray = []
    MoT = False

if len(rawInput2)>0:
    addArray = [int(num) for num in rawInput2.split(",")]
else:
    addArray = []

array = initialArray + addArray

array = arr
# print(array)

MoT_array = sorted([array[0], array[-1], array[int(len(array) / 2)]])
MoT = MoT_array[1]

# print(MoT)

left_heap = []
right_heap = []

for num in array:
    if num < MoT:
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)

# print(left_heap)
# print(right_heap)
# print(len(left_heap))
# print(len(right_heap))


adjustment = len(left_heap) - len(right_heap)

print(adjustment)

if adjustment > 0:
    for i in range(int(adjustment/2)):
        heapq.heappush(right_heap, -heapq.heappop(left_heap))
elif adjustment < 0:
    for i in range(int(-adjustment/2)):
        heapq.heappush(left_heap, -heapq.heappop(right_heap))


print(left_heap)
print(right_heap)
print(len(left_heap))
print(len(right_heap))
if len(left_heap) - len(right_heap) == 0:
    median = (-left_heap[0] + right_heap[0])/2
elif len(right_heap)>len(left_heap):
    median = right_heap[0]
else:
    median = -left_heap[0]

print("calcuated median: %d" %median)
print("actual median: %d" %statistics.median(array))
