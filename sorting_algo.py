##############################################
# Title: PA2 - Sorting Algorithms
# Author: Seunghyun Cho
# Version: 3.10.6
# Date: Feb 27th, 2023
#
# Description: This program implements sorting routines and analyzes the "work" of sorting routines.
##############################################
import numpy as np
import time
import pandas as pd
import copy
import sys

sys.setrecursionlimit(2000)

# selection_sort method
def selection_sort(array):
    swap = 0
    comparison = 0
    start = time.time()

    # set i to go through all the elements
    for i in range(0, len(array)-1):
        sm = i
        for j in range(i+1, len(array)):
            comparison += 1
            # if there is smaller element than ith value, then update sm as j
            if array[j] < array[sm]:
                sm = j
        # if there is smaller element, swap it
        if i != sm:
            temp = array[i]
            array[i] = array[sm]
            array[sm] = temp
            swap += 1
    end = time.time()
    result = [end-start, comparison, swap]
    return result

# bubble_sort method
# comparing data right next to each other
def bubble_sort(array):
    swap = 0
    comparison = 0
    start = time.time()

    # outer loop
    for i in range(0, len(array) - 1):
        # inner loop
        for j in range(0, len(array) - i - 1):
            comparison += 1
            if array[j] > array[j+1]:
                # if the next element is smaller, swap it
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                swap = swap + 1
    end = time.time()
    result = [end-start, comparison, swap]
    return result

# insertion_sort method
def insertion_sort(array):
    swap = 0
    comparison = 0
    start = time.time()

    # start from 2nd index
    for i in range(1, len(array)):
        j = i
        comparison += 1
        # if previous data is smaller than current data, swap it
        while j > 0 and array[j-1] > array[j]:
            comparison += 1
            temp = array[j]
            array[j] = array[j-1]
            array[j-1] = temp
            swap = swap + 1
            j -= 1
    end = time.time()
    result = [end-start, comparison, swap]
    return result

# shell_sort method
# use gap to sort
def shell_sort(array):
    swap = 0
    comparison = 0
    start = time.time()

    gap = len(array)//2

    while gap >= 1:
        for k in range(0, gap):
            for i in range(k + gap, len(array), gap):
                j = i

                comparison += 1
                while (j-gap) >= 0 and array[j-gap] > array[j]:
                    comparison += 1
                    temp = array[j]
                    array[j] = array[j-gap]
                    array[j-gap] = temp
                    swap = swap + 1

                    j = j - gap

        gap = gap // 2

    end = time.time()
    result = [end-start, comparison, swap]
    return result

# Merge sort class
# split all elements and rejoin while sorting
class Merge:
    def __init__(self):
        self.comparison = 0
        self.swap = 0
        self.start = time.time()

    # split the data and use recursion to sort
    def merge_sort(self, array):
        if len(array) <= 1:
            return
        mid = len(array) // 2

        left = array[:mid].copy()
        right = array[mid:].copy()

        self.merge_sort(left)
        self.merge_sort(right)
        self.merge(array, left, right)
        end = time.time()
        result = [end - self.start, self.comparison, self.swap]
        return result

    # merging split data
    def merge(self, array, lefthalf, righthalf):
        i = 0
        j = 0
        k = 0

        self.comparison += 2
        while i < len(lefthalf) and j < len(righthalf):
            self.comparison += 2
            self.comparison += 1
            if lefthalf[i] <= righthalf[j]:
                array[k] = lefthalf[i]
                i = i + 1
            else:
                array[k] = righthalf[j]
                self.swap += 1
                j += 1
            k += 1

        self.comparison += 1
        while i < len(lefthalf):
            self.comparison += 1
            array[k] = lefthalf[i]
            self.swap += 1
            i += 1
            k += 1

        self.comparison += 1
        while j < len(righthalf):
            self.comparison += 1
            array[k] = righthalf[j]
            j += 1
            k += 1

# Quick sort class
class Quick:
    def __init__(self):
        self.comparison = 0
        self.swap = 0
        self.start = time.time()
        self.end = 0

    # split data
    def partition(self, array, start_index, end_index):
        pivot_value = array[start_index]
        left_mark = start_index + 1
        right_mark = end_index

        while True:
            self.comparison += 2
            while left_mark <= right_mark and array[left_mark] <= pivot_value:
                self.comparison += 2
                left_mark += 1

            self.comparison += 2
            while array[right_mark] >= pivot_value and right_mark >= left_mark:
                self.comparison += 2
                right_mark -= 1
            self.comparison += 1
            if right_mark < left_mark:
                break
            else:
                temp = array[left_mark]
                array[left_mark] = array[right_mark]
                array[right_mark] = temp
                self.swap = self.swap + 1

        if start_index != right_mark:
            self.swap += 1
        array[start_index] = array[right_mark]
        array[right_mark] = pivot_value
        return right_mark

    def quick_sort(self, array):
        self.quick_sort_helper(array, 0, len(array) - 1)
        self.end = time.time()
        result = [self.end - self.start, self.comparison, self.swap]
        return result

    def quick_sort_helper(self, array, start_index, end_index):
        if start_index < end_index:
            split_point = self.partition(array, start_index, end_index)

            self.quick_sort_helper(array, start_index, split_point - 1)
            self.quick_sort_helper(array, split_point + 1, end_index)

def main():
    n = [250, 500, 1000]
    multi_list = []
    metrics = []

    # make data list to sort
    # ascending order
    for i in range(3):
        list_a = np.random.randint(3000, size = n[i])
        list_a.sort()
        list_a.tolist()
        multi_list.append(list_a)

    # descending order
    for i in range(3):
        list_d = np.random.randint(3000, size = n[i])
        list_d.sort()
        descending_list = list_d[::-1]
        descending_list.tolist()
        multi_list.append(descending_list)

    # random order
    for i in range(3):
        list_r = np.random.randint(3000, size = n[i])
        list_r.tolist()
        multi_list.append(list_r)


    for i in range(len(multi_list)):
        test_list = copy.deepcopy(multi_list)
        test_list2 = copy.deepcopy(multi_list)
        test_list3 = copy.deepcopy(multi_list)
        test_list4 = copy.deepcopy(multi_list)
        test_list5 = copy.deepcopy(multi_list)
        test_list6 = copy.deepcopy(multi_list)
        temp_list = selection_sort(test_list[i])
        temp_list.extend(bubble_sort(test_list2[i]))
        temp_list.extend(insertion_sort(test_list3[i]))
        temp_list.extend(shell_sort(test_list4[i]))
        m = Merge()
        temp_list.extend(m.merge_sort(test_list5[i]))
        q = Quick()
        temp_list.extend(q.quick_sort(test_list6[i]))
        metrics.append(temp_list)

    col = [["Selection Sort", "", "", "Bubble Sort", "", "", "Insertion Sort", "", "", "Shell Sort", "", "", "Merge Sort", "", "", "Quick Sort", "", ""], ["Time", "Data Comparisons", "Data Swaps", "Time", "Data Comparisons", "Data Swaps", "Time", "Data Comparisons", "Data Swaps", "Time", "Data Comparisons", "Data Swaps", "Time", "Data Comparisons", "Data Swaps", "Time", "Data Comparisons", "Data Swaps"]]
    ind = ["Ascending_Sorted_250", "Ascending_Sorted_500", "Ascending_Sorted_1000", "Descending_Sorted_250", "Descending_Sorted_500", "Descending_Sorted_1000", "Random_Sorted_250", "Random_Sorted_500", "Random_Sorted_1000"]
    df = pd.DataFrame(metrics, columns = col, index = ind)
    df.transpose()
    df.to_csv("sort_results.csv")


main()