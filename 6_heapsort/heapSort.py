#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To heapify subtree rooted at index i.
# n is size of heap

def heapify(arr, n, i):
    largest = i # Initialize largest as root.
    # Because array start with 0.
    l = 2 * i + 1
    r = 2 * i +2

    # See if left child of root exists and is greater than root.
    if l < n and arr[largest] < arr[l]:
        largest = l
    
    # See if right child od root exists and is greater than root.
    if r < n and arr[largest] < arr[r]:
        largest = r
    
    # Change root (if needed)
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Heapify the root.
        heapify(arr, n, largest)

# The main function to sort an array of given size.

def heapSort(arr):
    n = len(arr)

    # Build a maxheap
    for i in range(n//2 -1, -1, -1):
        heapify(arr, n, i)
    
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    heapSort(arr)
    print('Sorted array is')
    for i in range(len(arr)):
        print('%d' % arr[i])
