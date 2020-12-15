#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random

def partition(items, p, r):
    x = items[r]
    i = p -1
    for j in range(p, r):
        if items[j] <= x:
            i = i+1
            items[i], items[j] = items[j], items[i]
    items[i+1] , items[r] = items[r] ,items[i+1]
    return i+1

def randomizedPartition(items, p, r):
    i = random.randint(p, r)
    items[i], items[r] = items[r], items[i]
    return partition(items, p, r)

def randomizedQuickSort(items, p, r):
    if p < r:
        q = randomizedPartition(items, p, r)
        randomizedQuickSort(items, p , q-1)
        randomizedQuickSort(items, q+1, r)

if __name__ == '__main__':
    items = [2, 5, 9, 3, 7, 0, -1]
    randomizedQuickSort(items, 0, len(items)-1)
    print(items)