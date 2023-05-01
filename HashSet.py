import random


class Set:
    def __init__(self):
        self.slot_size = 11
        #self.table = HashTable(self.slot_size)

    def add(self, item):
        slot_present = self.table.get(item)
        if slot_present == -1:
            self.table.put(item)

    def remove(self, item):
        slot = self.table.remove(item)

    def pop(self):
        if self.size <= 0:
            raise Exception("Set is empty")
        else:
            slot = random.randint(0, self.slot_size - 1)
            while (self.table.slots[slot] == None):
                slot += 1
                if (slot >= self.slot_size):
                    slot = 0
                item = self.table.slots[slot]
                self.remove(item)
                return item

    def size(self):
        return self.table.size()

    def __contains__(self, item):
        if self.table.get(item) >= 0:
            return True
        else:
            return False

    def __iter__(self):
        return self.table.__iter__()

    def union(self, other):
        new_set = Set()
        for item in self:
            new_set.add(item)
        for item in other:
            new_set.add(item)
        return new_set

    def intersection(self, other):
        new_set = Set()
        for item in self:
            if item in other:
                new_set.add(item)
        return new_set

    def difference(self, other):
        new_set = Set()
        for item in self:
            if item not in other:
                new_set.add(item)
        return new_set
