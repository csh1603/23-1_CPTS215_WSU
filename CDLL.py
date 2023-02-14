##############################################
# Title: Participation Activity - Singly Linked List
# Author: Seunghyun Cho
# Version: 3.10.6
# Date: Feb 12th, 2023
#
# Description: This program implements a circular double linked list
##############################################

# Node class that contains data
class Node:
    def __init__(self, value = 0):
        self.data = value
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.data)

# CDLL class
class CDLL:
    # initialization function (needed)
    def __init__(self):
        self.head = None
        self.length = 0

    # return all data in list in string type
    def __str__(self):
        if self.length == 0:
            list_str = "None"
        else:
            cur_node = self.head
            i = 0
            list_str = " <-> " + str(cur_node.data)
            while cur_node.next is not self.head:
                if cur_node.next is None:
                    break
                cur_node = cur_node.next
                list_str += " <-> " + str(cur_node.data)
            list_str += " <->"
        return list_str

    # add new data (head part)
    def add(self, item):
        temp_node = Node(item)
        # if there is no data in list, add data as a head data
        if self.length == 0:
            self.head = temp_node
            self.head.prev = self.head
            self.head.next = self.head
        # if there was data, add data in front of existed data + make connection
        else:
            self.head.prev.next = temp_node
            temp_node.prev = self.head.prev
            self.head.prev = temp_node
            temp_node.next = self.head
            self.head = temp_node
        self.length += 1

    # add data at the last part of list
    def append(self, item):
        # if there is no data in list, add data as a head data
        if self.length == 0:
            self.head = Node(item)
            self.head.next = self.head
            self.head.prev = self.head
        # if there was data, add data at the last part of list
        else:
            # follow the list
            cur_node = self.head.prev
            # make new Node and name it as temp
            temp = Node(item)
            # last data will become the new node made above
            # make a connection (doubly linked list)
            temp.prev = cur_node
            cur_node.next = temp
            temp.next = self.head
            self.head.prev = temp
        self.length += 1

    # function that puts data between two data
    def insert(self, index, item):
        # if there is no data in list, just add the data
        temp = Node(item)
        if self.length == 0:
            self.head = temp
            self.head.prev = self.head
            self.head.next = self.head
            self.length += 1
            return
        if index == 0:
            temp.next = self.head
            temp.prev = self.head.prev
            self.head.prev = temp
            self.head.prev.next = temp
            self.head = temp
            self.length += 1
            return
        else:
            i = 0
            cur_node = self.head
            while cur_node.next is not self.head and i < index:
                cur_node = cur_node.next
                i += 1
            if cur_node.next is self.head:
                self.append(item)
                return
            else:
                temp.next = cur_node.next
                temp.prev = cur_node
                cur_node.next.prev = temp
                cur_node.next = temp
                self.length += 1
                return

    # function that pops data
    def pop(self, index = None):
        # if there is no data, return None
        if self.head is None:
            return None

        # if the user did not set the index number, pop the last element
        if index is None:
            index = self.length - 1

        # if the user set the index as 0
        if index == 0:
            # make head into second element and return first one
            cur_node = self.head
            tail_node = self.head.prev
            self.head = cur_node.next
            tail_node.next = self.head
            self.head.prev = tail_node
            cur_node.next = None
            cur_node.prev = None
            self.length -= 1
            return cur_node

        # if the user set the index not 0
        else:
            # start with the first element
            cur_node = self.head
            i = 1
            # repeat until meets index or the end of linked list
            while cur_node.next is not self.head and i < index:
                cur_node = cur_node.next
                i += 1
            # set pop data as to_pop
            if cur_node.next is not self.head:
                to_pop = cur_node.next
                # if there is more data next to to_pop
                if to_pop.next is not self.head:
                    to_pop.next.prev = cur_node
                    cur_node.next = to_pop.next
                    to_pop.next = None
                    to_pop.prev = None
                # if there is no more data after to_pop
                else:
                    cur_node.next = self.head
                    self.head.prev = cur_node
                    to_pop.prev = None
                    to_pop.next = None
                self.length -= 1
                return to_pop

    # function that finds item and deletes
    def remove(self, item):
        # if there is no data
        if self.head is None:
            print("DLL is empty.")
            return None

        # variables to follow the list
        cur_node = self.head
        prev_node = self.head.prev
        next_node = self.head.next
        found = False
        i = 0

        # repeat until find the data or meet the end of list
        while i < self.length and not found:
            # if we found the data
            if cur_node.data == item:
                found = True
            # if we did not find the data -> keep going
            else:
                prev_node = cur_node
                cur_node = next_node
                next_node = next_node.next
            i += 1

        # if we found the data (found is True)
        if found:
            # targeted data is first data
            if cur_node is self.head:
                if next_node is not self.head:
                    next_node.prev = self.head.prev
                    self.head.prev.next = next_node
                    cur_node.prev = None
                    cur_node.next = None
                    self.head = next_node
                else:
                    self.head = None
            # targeted data is before the head pointer
            elif cur_node is self.head.prev:
                if prev_node is not self.head:
                    prev_node.next = self.head
                    self.head.prev = prev_node
                    cur_node.prev = None
                    cur_node.next = None
                else:
                    self.head.prev = self.head
                    self.head.next = self.head
            else:
                prev_node.next = cur_node.next
                prev_node.next = next_node
                next_node.prev = prev_node
                cur_node.prev = None
                cur_node.next = None
            self.length -= 1
        return found

    # function that finds item in the list
    def search(self, item):
        # set first data as cur_node
        cur_node = self.head
        found = -1
        loc = 0

        # repeat until the data is found
        while found == -1:
            # if data is found, update found variable as a location of data
            # it will escape the while loop
            if cur_node.data == item:
                found = loc
            else:
                if cur_node.next is self.head:
                    break
                cur_node = cur_node.next
            loc += 1

        return found

    # function that returns the data at the location of index
    def __getitem__(self, index):
        i = 0
        # set cur_node as first data
        cur_node = self.head
        # if the user inputs index that is larger than we have or a negative value, raise exception
        if index >= self.length or index < 0:
            raise IndexError("Index out of range")
        while i < index and cur_node.next is not self.head:
            cur_node = cur_node.next
            i += 1
        return cur_node.data

    # function that changes [index] data into item
    def __setitem__(self, index, item):
        i = 0
        cur_node = self.head
        if index >= self.length or index < 0:
            raise IndexError("Index out of range")
        while i < index and cur_node.next is not self.head:
            cur_node = cur_node.next
            i += 1
        # changes data
        cur_node.data = item

    # functions that delete data at the location of index
    def __delitem__(self, index):
        self.pop(index)

    # function that shows whether it is empty or not
    def is_empty(self):
        return self.length == 0

    # function that shows how many data are contained
    def size(self):
        return self.length

    # function that shows how many data are contained
    def __len__(self):
        return self.size()

    # function that returns and iterator object created by the generator method
    def __iter__(self):
        return self.generator()

    # function that creates a reference for forward iteration
    def generator(self):
        cur_node = self.head
        i = 0
        while (i < self.length):
            yield cur_node.data
            if cur_node.next is self.head:
                break
            cur_node = cur_node.next
            i += 1

    # function that print data in the reversed way
    def __reversed__(self):
        cur_node = self.head.prev
        i = self.length
        # after we reach the end, print each data and go back to previous data
        while (i > 0):
            yield cur_node.data
            cur_node = cur_node.prev
            i -= 1

# Main method testing the circular doubly Linked List with sample data
def main():
    dll = CDLL()
    # Generate sample data and add to the circular doubly linked list
    for i in range(100, 200, 11):
        dll.add(i)
    print("circular doubly linked list after add operations:")
    print(dll, "\n")
    for i in range(100, 200, 11):
        print("index for", i, ": ", dll.search(i))
    print("\n")
    # Remove sample data from circular doubly linked list using remove() method
    for j in range(100, 200, 11):
        dll.remove(j)
    print("circular doubly linked list after remove operations:")
    print(dll, "\n")
    # Generate sample data and append to the circular doubly linked list
    for i in range(200, 300, 11):
        dll.append(i)
    print("circular doubly linked list after append operations:")
    print(dll, "\n")
    # Remove and print sample data from circular doubly linked list using pop() method
    print("circular doubly linked list items removed during pop operations:")
    for j in range(0, len(dll)):
        print(dll.pop(), end = ", ")
    print("\n\ncircular doubly linked list after pop operations:")
    print(dll, "\n")
    # Generate sample data and insert it to the circular doubly linked list
    index = 0
    for i in range(300, 400, 11):
        dll.insert(index, i)
        index += 1
    print("circular doubly linked list after insert operations:")
    print(dll, "\n")
    # Remove and print sample data from circular doubly linked list using pop() method
    print("circular doubly linked list items removed during pop operations:")
    for j in range(0, len(dll)):
        print(dll.pop(), end = ", ")
    print("\n\ncircular doubly linked list after pop operations:")
    print(dll, "\n")
    # Generate sample data and append to the circular doubly linked list
    for i in range(400, 500, 11):
        dll.append(i)
    print("circular doubly linked list after append operations:")
    print(dll, "\n")
    # Get data from circular doubly linked list using indexing
    print("circular doubly linked list data elements accessed using indexing:")
    for i in range(0, len(dll)):
        print(dll[i], end=", ")
    print("\n")
    # Update date in circular doubly linked list using indexing
    i = 0
    for j in range(500, 600, 11):
        dll[i] = j
        i += 1
    print("circular doubly linked list after update operations:")
    print(dll, "\n")
    # Delete data from circular doubly linked list using indexing
    for i in range(len(dll)-1, -1, -1):
        del(dll[i])
    print("circular doubly linked list after delete operations:")
    print(dll, "\n")
    # Check if circular doubly linked list is empty
    print("List is empty? : ", dll.is_empty(), "\n")
    # Generate sample data and append to the circular doubly linked list
    for i in range(600, 700, 11):
        dll.append(i)
    print("circular doubly linked list after append operations:")
    print(dll, "\n")
    # Get data from circular doubly linked list using an Iterator
    print("circular doubly linked list elements using iterator:")
    for data in dll:
        print("node: " + str(data), end=", ")
    print("\n")
    # Get data in reverse from circular doubly linked list using an Iterator
    print("circular doubly linked list elements in reverse using iterator:")
    for data in reversed(dll):
        print("node: " + str(data), end=", ")
    print("\n")

if __name__ == "__main__":
    main()