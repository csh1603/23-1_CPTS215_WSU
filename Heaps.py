##############################################
# Title: PA4 - Heaps
# Author: Seunghyun Cho
# Version: 3.10.6
# Date: Mar 25th, 2023
#
# Description: This program implements Binary max-Heap and Ternart max-Heap.
##############################################

# class for Binary Max Heap - maximum value has the priority
class BinaryMaxHeap:
    # initialization method
    def __init__(self):
        # make 1st index as 0 so to find the child & parent easily
        self.heap_list = [0]
        self.size = 0

    # show the data as string type
    def __str__(self):
        if self.size == 0:
            return None
        str = ""
        i = 1
        while i <= self.size:
            str += self.heap_list[i] + " "
            i += 1
        return str

    # show how many data are in
    def __len__(self):
        return self.size

    # method finds if item is in the list
    def __contains__(self, item):
        i = 1
        while i <= self.size:
            if item == self.heap_list[i]:
                return True
            i += 1
        return False

    # return the list is empty
    def is_empty(self):
        return self.size == 0

    # find the maximum value -> return the first value
    def find_max(self):
        if self.size > 0:
            return self.heap_list[1]
        return None

    # insert data and reorganize
    def insert(self, item):
        self.heap_list.append(item)
        self.size += 1
        self.percolate_up(self.size)

    # method helps data organizing
    def percolate_up(self, index):
        # keep track of the parent data
        while index // 2 > 0:
            # if the child value is greater than the parent value, swap
            if self.heap_list[index] > self.heap_list[index // 2]:
                temp = self.heap_list[index // 2]
                self.heap_list[index // 2] = self.heap_list[index]
                self.heap_list[index] = temp
            index //= 2

    # method that delete the maximum value
    def del_max(self):
        max_value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.heap_list.pop()
        self.size -= 1
        # reorganize the list
        self.percolate_down(1)
        return max_value

    # method helps data organizing
    def percolate_down(self, index):
        # repeat until there is no child node
        while (index * 2) <= self.size:
            max_child = self.max_child(index)
            # if the parent's data is less than child's data, swap
            if self.heap_list[index] < self.heap_list[max_child]:
                temp = self.heap_list[index]
                self.heap_list[index] = self.heap_list[max_child]
                self.heap_list[max_child] = temp
            index = max_child

    # method let us know which node has the maximum value among children nodes
    def max_child(self, index):
        # if there is only left child
        if index * 2 + 1 > self.size:
            return index * 2
        else:
            # if the left child is greater than the right child, then return left child's index
            if self.heap_list[index * 2] > self.heap_list[index * 2 + 1]:
                return index * 2
            # if the right child is greater than the left child, then return right child's index
            else:
                return index * 2 + 1

    # method that builds a max-heap from a list
    def build_heap(self, alist):
        self.heap_list = [0] + alist[:]
        self.size = len(alist)
        index = len(alist) // 2
        while index > 0:
            self.percolate_down(index)
            index -= 1

# Ternary Max Heap class for nodes which have 3 children
class TernaryMaxHeap:
    # initialization method
    def __init__(self):
        # make 1st index as 0 so to find the child & parent easily
        self.heap_list = [0]
        self.size = 0

    # show the data as string type
    def __str__(self):
        if self.size == 0:
            return None
        str = ""
        i = 1
        while i <= self.size:
            str += self.heap_list[i] + " "
            i += 1
        return str

    # show how many data are in
    def __len__(self):
        return self.size

    # method finds if item is in the list
    def __contains__(self, item):
        i = 1
        while i <= self.size:
            if item == self.heap_list[i]:
                return True
            i += 1
        return False

    # return the list is empty
    def is_empty(self):
        return self.size == 0

    # find the maximum value -> return the first value
    def find_max(self):
        if self.size > 0:
            return self.heap_list[1]
        return None

    # insert data and reorganize
    def insert(self, item):
        self.heap_list.append(item)
        self.size += 1
        self.percolate_up(self.size)

    # method helps data organizing
    def percolate_up(self, index):
        # keep track of the parent data
        while (index - 2) // 3 + 1 > 0:
            # if the child value is greater than the parent value, swap
            if self.heap_list[index] > self.heap_list[(index - 2) // 3 + 1]:
                temp = self.heap_list[(index - 2) // 3 + 1]
                self.heap_list[(index - 2) // 3 + 1] = self.heap_list[index]
                self.heap_list[index] = temp
            index = (index - 2) // 3 + 1

    # method that deletes the maximum value
    def del_max(self):
        max_value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.heap_list.pop()
        self.size -= 1
        # reorganize the list
        self.percolate_down(1)
        return max_value

    # method helps data organizing
    def percolate_down(self, index):
        # repeat until there is no child node
        while (index * 3 - 1) <= self.size:
            max_child = self.max_child(index)
            # if the parent's data is less than child's data, swap
            if self.heap_list[index] < self.heap_list[max_child]:
                temp = self.heap_list[index]
                self.heap_list[index] = self.heap_list[max_child]
                self.heap_list[max_child] = temp
            index = max_child


    # method let us know which node has the maximum value among children nodes
    def max_child(self, index):
        # if there is only left child
        if index * 3 > self.size:
            return index * 3 - 1
        # if there are left and middle child
        if index * 3 + 1> self.size:
            if self.heap_list[index * 3 - 1] > self.heap_list[index * 3]:
                return index * 3 - 1
            else:
                return index * 3
        # if there are left and middle and right child
        else:
            if self.heap_list[index * 3 - 1] > self.heap_list[index * 3]:
                if self.heap_list[index * 3 - 1] > self.heap_list[index * 3 + 1]:
                    return index * 3 - 1
                else:
                    return index * 3 + 1
            else:
                if self.heap_list[index * 3] > self.heap_list[index * 3 + 1]:
                    return index * 3
                else:
                    return index * 3 + 1

    # method that builds a max-heap from a list
    def build_heap(self, alist):
        self.heap_list = [0] + alist[:]
        self.size = len(alist)
        index = (len(alist) - 2) // 3 + 1
        while index > 0:
            self.percolate_down(index)
            index -= 1

print("Test Binary Max Heap")
bmh = BinaryMaxHeap()
bmh.insert("Z")
bmh.insert("Y")
bmh.insert("X")
bmh.insert("W")
bmh.insert("V")
bmh.insert("U")
bmh.insert("T")

print(bmh)
print("maximum value: ", bmh.del_max())
print("after deleting maximum value: ", bmh)

bmh.insert("Z")
print("after inserting Z: ", bmh)

bmh = BinaryMaxHeap()
alist = ["B", "H", "C", "A", "Z", "X"]
bmh.build_heap(alist)
print(bmh)

print("\nTest Ternary Max Heap")
tmh = TernaryMaxHeap()
tmh.insert("Z")
tmh.insert("Y")
tmh.insert("X")
tmh.insert("W")
tmh.insert("V")
tmh.insert("U")
tmh.insert("T")
tmh.insert("S")
tmh.insert("R")
tmh.insert("Q")
tmh.insert("P")
tmh.insert("O")
tmh.insert("N")
print(tmh)

print("maximum value: ", tmh.del_max())
print("after deleting maximum value: ", tmh)

tmh.insert("Z")
print("after inserting Z: ", tmh)

tmh = TernaryMaxHeap()
alist = ["B", "H", "C", "A", "Z", "X", "D", "Y"]
tmh.build_heap(alist)
print(tmh)
