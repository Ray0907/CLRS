#!/usr/bin/python3
# -*- coding: utf-8 -*-

def countSort(arr, min, max):
    
    # Init
    count_dict = {}
    cumulativeSum_dict = {}
    sorted = []
    for i in range(min,max+1):
        count_dict[i] = 0
        cumulativeSum_dict[i] = 0

    for index, num in enumerate(arr):
        if num in count_dict.keys():
            count_dict[num] +=1
        else:
            count_dict[num] = 1
    
    sum = 0
    for i in count_dict.keys():
        sum += count_dict[i]
        cumulativeSum_dict[i] = sum
        
    for index, data in enumerate(cumulativeSum_dict.keys()):
        if index > 0:
            if(cumulativeSum_dict[data] == cumulativeSum_dict[data -1]):
                continue
            else:
                count = cumulativeSum_dict[data] - cumulativeSum_dict[data -1]
                for i in range(count):
                    sorted.extend(data)
        else:
            count = cumulativeSum_dict[data]
            for i in range(count):
                sorted.extend(data)
    return sorted

if __name__ == '__main__':
    arr = [7, 9, 3, 2, 3, 1, 5, 1000, 247, 88, 963]
    min = min(arr)
    max = max(arr)
    print(countSort(arr, min, max))



