#!/usr/bin/python3
# -*- coding: utf-8 -*-

def insertionSort(s):
    for i in range(1, len(s)):
        up = s[i]
        j = i -1
        while j >=0 and s[j] > up:
            s[j+1] = s[j]
            j -= 1
        s[j+1] = up
    return s

def bucketSort(arr):
    arr_new = []
    slot_num = 10 # 10 means 10 slots, each slot's size is 0.1 
    
    for i in range(slot_num):
        arr_new.append([])
    
    # Put array elements in different buckets.
    for i in arr:
        index = int(slot_num * i)
        arr_new[index].append(i)
    
    # Sort individual buckets
    for i in range(slot_num):
        arr_new[i] = insertionSort(arr_new[i])

    k = 0
    for i in range(slot_num):
        for j in range(len(arr_new[i])):
            arr[k] = arr_new[i][j]
            k += 1
    
    return arr

if __name__ == '__main__':
    array = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]  
    print('Sorte array is')
    print(bucketSort(array))