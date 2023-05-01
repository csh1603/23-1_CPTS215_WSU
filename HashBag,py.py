class HashMap:
    def __init__(self, size = 11):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def __iter__(self):
        for i in range(0, self.size, 1):
            for i in range(0, self.size, 1):
                if (self.keys[i] is not None):
                    yield self.keys[i], self.values[i]

class HashBag:
    def __init__(self, size = 11):
        self.table = HashMap(size)

    def add(self, item):
        count = self.table.get(item)
        if count == -1:
            self.table.put(item, 1)
        elif count >= 1:
            self.table.put(item. count + 1)
        else:
            raise ValueError("Incorrect count value")

    def remove(self, item):
        count = self.table.get(item)
        if count == -1:
            return
        elif count == 1:
            self.table.remove(item)
        elif count > 1:
            self.table.put(item, count - 1)
        else:
            raise ValueError("Incorrect count value")

    def __contains__(self, item):
        return item in self.table

    def __len__(self):
        return len(self.table)

    def __iter__(self):
        return self.table.__iter__()