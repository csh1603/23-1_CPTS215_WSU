##############################################
# Title: Participation Activity - Singly Linked List
# Author: Seunghyun Cho
# Version: 3.10.6
# Date: Feb 5th, 2023
#
# Description: This program implements a singly linked list with head and tail nodes
##############################################

# Node class that contains data
class Node:
    # when Node class is made, it means that it is the last data -> self.next = None
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

# Linked List class that makes list of node
class LinkedList:
    # when the linked list is first made it has no information in it
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # adding new node
    def add(self, item):
        # make new node that contains item as a data and call it as temp
        temp = Node(item)
        # temp is the last data so update as a head
        temp.next = self.head
        # if there is no data, make temp as a tail
        if self.tail is None:
            self.tail = temp
        self.head = temp
        self.size = self.size + 1

    # function that finds the index of value
    def search(self, item):
        # set first data as current
        current = self.head
        found = -1
        loc = 0

        # repeat until the data is found
        while current is not None and found == -1:
            # if data is found, update found variable as a location of data
            # it will escape the while loop
            if current.data == item:
                found = loc
            else:
                current = current.next
            loc += 1

        return found

    # function that removes data
    def remove(self, item):
        # set first data as current
        current = self.head
        previous = None
        found = False

        # repeat until the data is found
        while current is not None and not found:
            # if data is found, set found as True and escape while loop
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next

        # if we found the data
        if found:
            # if the targeted data is head, then we just have to remove the data
            if current == self.head:
                self.head = current.next
                current.next = None
            if current == self.tail:
                self.tail = previous
            # if the targeted data is not head, then we have to remove the data and make a connection between previous and after data
            else:
                previous.next = current.next
                current.next = None
                if current == self.tail:
                    self.tail = previous
            self.size -= 1

    # function that returns how many node are in linked list
    def size(self):
        return self.size

    # function that returns whether linked list is empty
    def is_empty(self):
        return self.head is None

    # print all data in linked list
    def __str__(self):
        list_str = ""
        current = self.head

        while current is not None:
            list_str += str(current.data)
            list_str += "->"
            current = current.next
        list_str += "None"

        return list_str

    # function that adds new data
    def append(self, item):
        # if there was no data in linked list, make new data as head
        if self.head is None:
            self.head = Node(item)
        # if there was more than 1 data
        else:
            # follow the list
            current = self.head
            while current.next is not None:
                current = current.next
            # make new Node and name it as temp
            temp = Node(item)
            # last data will become the new node made above
            current.next = temp
            self.tail = temp
        self.size = self.size + 1

    # function that insert data
    def insert(self, index, item):
        # if wanted location is first or there was no data in linked list
        if index == 0 or self.head is None:
            self.add(item)
        else:
            current = self.head
            i = 0
            # continue until there is no next data or it meets end of the linked list
            while current.next is not None and i < index - 1:
                current = current.next
                i += 1
            # make new Node named temp
            temp = Node(item)
            # insert data into [index]
            temp.next = current.next
            current.next = temp
        self.size = self.size + 1

    # function that return data and remove it
    def pop(self, index = None):
        # if there is no data, return None
        if self.head is None:
            return None

        # if the user did not set the index number, pop the last element
        if index is None:
            index = self.size - 1

        # if the user set the index as 0
        if index == 0:
            # make head into second element and return first one
            current = self.head
            self.head = self.head.next
            current.next = None
            self.size = self.size - 1
            return current

        # if the user set the index not 0
        else:
            # start with the first element
            current = self.head
            i = 1
            # repeat until meets index or the end of linked list
            while current.next is not None and i < index:
                current = current.next
                i += 1
            # set pop data as to_pop
            to_pop = current.next
            # connect to_pop's previous and after data
            current.next = to_pop.next
            to_pop.next = None
            self.size = self.size - 1
            return to_pop
