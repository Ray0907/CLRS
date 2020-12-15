#!/usr/bin/python3
# -*- coding: utf-8 -*-

def partition(items, p, r):
    x = items[p]
    i = p - 1
    j = r + 1

    while True:
        
        while True:
            j = j - 1
            if items[j] <= x:
                break
        while True:
            i = i + 1
            if items[i] >= x:
                break
        if i < j:
            items[i],items[j] = items[j],items[i]
        else:
            return j

def quickSort(items, p, r):
    if p < r:
        q = partition(items, p, r)
        quickSort(items, p, q)
        quickSort(items, q+1, r)

if __name__ == '__main__':
    items = [13,19,9,5,12,8,7,4,11,2,6,21]
    quickSort(items, 0, len(items) -1)
    print(items)
