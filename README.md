# findMedian_MaxMinHeap

Given an array of n integers. We are allowed to add k additional integer in the array
and then find the median of the resultant array. We can choose any k values to be
added.

Interger array can be added repetitively.
New values are pushed into heaps and median if found efficiently.

The program is implented using Max Min Heap.
Got the BASIC idea from:
https://stackoverflow.com/questions/11361320/data-structure-to-find-median

note: if size of input is even, the middle 2 numbers are averaged

Test and checking function is included in the main file.
Test data is generated using numpy.random.rand()
Checking is done using statistics.median()