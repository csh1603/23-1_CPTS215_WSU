import time

def bubble_sort(array):
    swap = 0
    comparison = 0
    start = time.time()

    for i in range(0, len(array) - 1):
        for j in range(0, len(array) - 1):
            comparison += 1
            if array[j] > array[j+1]:
                print("hi")
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                swap = swap + 1
    end = time.time()
    result = [array, end-start, comparison, swap]
    return result

def insertion_sort(array):
    swap = 0
    comparison = 0
    start = time.time()

    for i in range(1, len(array)):
        j = i

        comparison += 1
        while j > 0 and array[j-1] > array[j]:
            swap += 1
            comparison += 1
            temp = array[j]
            array[j] = array[j-1]
            array[j-1] = temp
            j -= 1
    end = time.time()
    result = [array, end-start, comparison, swap]
    return result

def shell_sort(array):
    swap = 0
    comparison = 0
    start = time.time()

    gap = len(array)//2

    comparison += 1
    while gap >= 1:
        comparison += 1
        for k in range(0, gap):
            for i in range(k + gap, len(array), gap):
                j = i

                comparison += 2
                while (j-gap) >= 0 and array[j-gap] > array[j]:
                    comparison += 2
                    temp = array[j]
                    array[j] = array[j-gap]
                    array[j-gap] = temp
                    swap = swap + 1

                    j = j - gap

        gap = gap // 2

    end = time.time()
    result = [array, end-start, comparison, swap]
    return result

class Merge:
    def __init__(self):
        self.comparison = 0
        self.swap = 0
        self.start = time.time()

    def merge_sort(self, array):
        self.comparison += 1
        if len(array) <= 1:
            return
        mid = len(array) // 2

        left = array[:mid].copy()
        right = array[mid:].copy()

        self.merge_sort(left)
        self.merge_sort(right)
        self.merge(array, left, right)
        end = time.time()
        result = [array, end - self.start, self.comparison, self.swap]
        return result

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

class Quick:
    def __init__(self):
        self.comparison = 0
        self.swap = 0
        self.start = time.time()
        self.end = 0

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

        array[start_index] = array[right_mark]
        array[right_mark] = pivot_value
        return right_mark

    def quick_sort(self, array):
        self.quick_sort_helper(array, 0, len(array) - 1)
        self.end = time.time()
        result = [array, self.end - self.start, self.comparison, self.swap]
        return result

    def quick_sort_helper(self, array, start_index, end_index):
        if start_index < end_index:
            split_point = self.partition(array, start_index, end_index)

            self.quick_sort_helper(array, start_index, split_point - 1)
            self.quick_sort_helper(array, split_point + 1, end_index)

pract = [500, 2, 2, 3, 400]
print(type(pract))
print(bubble_sort(pract))
print(insertion_sort(pract))
print(shell_sort(pract))
m = Merge()
print(m.merge_sort(pract))
q = Quick()
print(q.quick_sort(pract))
