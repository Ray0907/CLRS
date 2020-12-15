#!/usr/bin/python3
# -*- coding: utf-8 -*-

def partition(items, p, r):
    x = items[r]
    i = p - 1
    count = 0
    print(p, r)
    for j in range(p, r):
        if items[j] == x:
            count = count +1
        if items[j] <= x:
            i = i + 1
            items[i], items[j] = items[j], items[i]

        items[i+1], items[r] = items[r], items[i+1]

        return int(i+1- count /2)

def quickSort(items, p, r):
    if p < r:
        q = partition(items, p, r)
        quickSort(items, p, q-1)
        quickSort(items, q+1, r)

if __name__ == '__main__':
    items = [2, 5, 9, 3, 7, 0, -1]
    quickSort(items, 0, len(items)-1)
    print(items)
