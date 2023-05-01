class BSTNode:
    def __init__(self, key, val, left = None, right = None, parent = None):
        self.key = key
        self.value = val
        self.left_child = left
        self.right_chile = right
        self.parent = parent

class BinarySearchTreeMap:
    def __init__(self):
        self.root = None
        self.size = 0

    def __iter__(self):
        return self.iterator_helper(self.root)

    def iterator_helper(self, node):
        if node is not None:
            yield str(node.key), str(node.value)
            yield from self.iterator_helper(node.left_child)
            yield from self.iterator_helper(node.right_child)

class TreeBag:
    def __init__(self):
        self.tree = BinarySearchTreeMap

    def add(self, item):
        count = self.tree.get(item)
        if (count is None):
            self.tree.put(item, 1)
        elif count >= 1:
            self.tree.put(item, count + 1)
        else:
            raise ValueError("Incorrect count value")

    def remove(self, item):
        count = self.tree.get(item)
        if count is None:
            return
        elif count == 1:
            self.tree.remove(item)
        elif count > 1:
            self.tree.put(item, count - 1)
        else:
            raise ValueError("Incorrect count value")

    def __contains__(self, item):
        if self.tree.get(item) != None:
            return True
        else:
            return False

    def __len__(self):
        return len(self.tree)

    def __iter__(self):
        return self.tree.__iter__()