#!/usr/bin/python3
# -*- coding: utf-8 -*-


def partition(arr, low, high):
    i = low -1
    pivot = arr[high]

    for j in range(low, high):
        # If current element is smaller than the pivot
        if arr[j] < pivot:
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def quickSort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)

        quickSort(arr, low, p -1)
        quickSort(arr, p+1, high)

if __name__ == '__main__':
    arr = [10, 7, 8, 9, 1, 5]
    quickSort(arr, 0 ,len(arr) -1)
    print("Sorted array is: ")
    print(arr)

