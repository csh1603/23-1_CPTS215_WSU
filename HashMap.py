##############################################
# Title: PA5 - HashMap
# Author: Seunghyun Cho
# Version: 3.10.6
# Date: Apr 8th, 2023
#
# Description: This program implements a Map using Hash Tables
##############################################
import re
from DLL import *

class HashMap:
    # method for initializing
    def __init__(self, size = 11):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.total_count = 0

    # method print every key-value pair in HashMap
    def __str__(self):
        s = ""
        for slot, key in enumerate(self.keys):
            value = self.values[slot]
            s += str(key) + ":" + str(value) + ", "
        return s
    # method printing out how many pairs are in HashMap
    def __len__(self):
        return self.total_count

    # return whether there is key in HashMap
    def __contains__(self, key):
        return self.get(key) != -1

    # return corresponding value from key
    def __getitem__(self, key):
        return self.get(key)

    # adding key-value pair
    def __setitem__(self, key, value):
        self.put(key, value)

    # method removing key-value pair
    def __delitem__(self, key):
        self.remove(key)

    # method for find where to store data by using ascii code
    def hashfunction(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % self.size

    # put data
    def put(self, key, value):
        # find index number to store data
        hashvalue = self.hashfunction(key)

        # if there is no data, make new DLL and add key and value respectively
        if self.keys[hashvalue] == None:
            self.keys[hashvalue] = DLL()
            self.keys[hashvalue].append(key)
            self.values[hashvalue] = DLL()
            self.values[hashvalue].append(value)
        # if there are data already, find whether there is the same data as key
        else:
            i = self.keys[hashvalue].search(key)
            # there is no same data as key
            if i == -1:
                self.keys[hashvalue].append(key)
                self.values[hashvalue].append(value)
            # if there is already the same data exists, add 1 to the value
            else:
                j = self.values[hashvalue].get(i)
                self.values[hashvalue].put(i, j + 1)
        self.total_count += 1

    # method to find whether there is key data presenting
    def get(self, key):
        hashvalue = self.hashfunction(key)

        i = self.keys[hashvalue].search(key)
        # if there is no such data return -1
        if self.keys[hashvalue] is None or i == -1:
            return -1

        # if there is data, return value (how many words are exists)
        return self.values[hashvalue].get(i)

    # method for removing key data
    def remove(self, key):
        hashvalue = self.hashfunction(key)

        i = self.keys[hashvalue].search(key)
        # if there is no key value existing, return -1
        if i == -1:
            return -1
        # if there is only 1 for the value, remove the Node
        if self.values[hashvalue].get(i) == 1:
            self.keys[hashvalue].pop(i)
            self.values[hashvalue].pop(i)
        # if there is a value greater than 1, subtract 1 from the value
        else:
            j = self.values[hashvalue].get(i)
            self.values[hashvalue].put(i, j - 1)
        self.total_count -= 1

def main():
    map = HashMap()
    fname = input("Please enter a file name: ")
    f = open(fname, "r")

    lines = f.read()
    lines = lines.lower()
    # remove all special character except '
    lines = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", lines)
    # split lines into words
    lines = lines.split()
    # put each word to map
    for i in range(len(lines)):
        map.put(lines[i], 1)

    print("total count: ", map.total_count)

    # repeat until the user inputs 'q'
    while True:
        print()
        find = input("Try a word (enter 'Q' or 'q' to quit): ")
        if find.lower() == 'q':
            break
        j = map.get(find)
        if j == -1:
            print("Word '{0}' not found".format(find))
        else:
            print("Word '{0}' has a count of {1}".format(find, j))


if __name__ == "__main__":
    main()