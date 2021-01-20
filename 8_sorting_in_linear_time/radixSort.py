#!/usr/bin/python3
# -*- coding: utf-8 -*-

def countingSort(arr, exp):

    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0 for i in range(n)]

    # Initialize count array as 0
    count = [0] * (10)

    # Store count of occurences in count[]
    for i in range(0, n):
        index = (arr[i] / exp)
        count[int(index % 10 )] += 1

    # Change count[i] so that count[i] now contains actual position of this digit in output array.
    for i in range(1, 10):
        count[i] += count[i-1]

    # Build the output array
    i = n -1
    while i >=0:
        index = (arr[i]/ exp)
        output[count[int(index % 10)] -1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1
    
    # Copying the output array to arr[]
    # So that arr now contains sorted numbers.
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

def radixSort(arr):
    # Find the maxumum number to know number of digits
    largest = max(arr)

    # Do counting sort for every digit. Note that instead 
    # of passing digit number, exp is passed. exp is 10^i 
    # where i is current digit number 
    exp = 1
    while largest / exp > 0:
        countingSort(arr, exp)
        exp *= 10

if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66] 
    radixSort(arr)
    for i in range(len(arr)):
        print(arr[i])