import time

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
        result = [array, self.end - self.start, self.comparison, self.swap]
        return result

    def quick_sort_helper(self, array, start_index, end_index):
        if start_index < end_index:
            split_point = self.partition(array, start_index, end_index)

            self.quick_sort_helper(array, start_index, split_point - 1)
            self.quick_sort_helper(array, split_point + 1, end_index)

des = [1, 2 ,9, 4, 5]
q = Quick()
print(q.quick_sort(des))