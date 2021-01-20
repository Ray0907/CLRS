#!/usr/bin/python3
# -*- coding: utf-8 -*-

def partition(items, p, r):
    x = items[r]
    i = p -1
    
    for j in range(p, r):
        if(items[j] <= x):
            i = i +1
            items[i], items[j] = items[j], items[i]
    
    items[i+1], items[r] = items[r], items[i+1]
    
    return i+1

def tailQuickSort(items, p, r):
    while p <r:
        q = partition(items, p, r)
        if (r - q) >= (q - p):
            tailQuickSort(items, p, q-1)
            p = q + 1
        else:
            tailQuickSort(items, q+1, r)
            r = q -1

if __name__ == '__main__':
    items = [2, 5, 9, 3, 7, 0, -1]
    tailQuickSort(items, 0, len(items) -1)
    print(items)
