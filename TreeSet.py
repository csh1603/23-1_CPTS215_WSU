class Set:
    def __init__(self):
        pass
        #self.tree = BinarySearchTree()

    def add(self, item):
        self.tree.put(item, item)

    def remove(self, item):
        self.tree.delete(item)

    def pop(self):
        if self.size() <= 0:
            raise KeyError("Set is empty")
        else:
            item = self.tree.root.key
            self.tree.delete(item)
            return item

    def __contains__(self, item):
        if self.tree.get(item) != None:
            return True
        else:
            return False

    def size(self):
        return self.tree.length()

    def __iter__(self):
        return self.tree.__iter__()

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
            if item in other:
                new_set.add(item)
        return new_set
    