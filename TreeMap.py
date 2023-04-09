class BSTNode:
    def __init__(self, key, val, left = None, right = None, parent = None):
        self.key = key
        self.value = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def pre_order_traversal(self):
        if self.root is None:
            print("Empty Tree")
        else:
            self.pre_order_traversal_helper(self.root)
            print()

    def pre_order_traversal_helper(self, node):
        if node is None:
            return
        print(str(node.key) + ":" + str(node.value), end = "")
        self.pre_order_traversal_helper(node.left_child)
        self.pre_order_traversal_helper(node.right_child)

    def get(self, key):
        if self.root is None:
            return None
        else:
            node = self._get(key, self.root)
            if node is not None:
                return node.value
            else:
                return None

    def _get(self, key, curr_node):
        if curr_node is None:
            return None
        else:
            if key == curr_node.key:
                return curr_node
            if key < curr_node.key:
                return self._get(key, curr_node.left_child)
            else:
                return self._get(key, curr_node.right_child)

    def put(self, key, value):
        if self.root is None:
            self.root = BSTNode(key, value)
            self.size += 1
        else:
            self._put(key, value, self.root)

    def _put(self, key, value, curr_node):
        if key == curr_node.key:
            curr_node.value = value
            return
        elif key < curr_node.key:
            if curr_node.left_child is None:
                curr_node.left_child = BSTNode(key, value, parent = curr_node)
                self.size += 1
            else:
                self._put(key, value, curr_node.left_child)
        else:
            if curr_node.right_child is None:
                curr_node.right_child = BSTNode(key, value, parent = curr_node)
                self.size += 1
            else:
                self._put(key, value, curr_node.right_child)

    def delete(self, key):
        if self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        elif self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove is not None:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError("Error, data not present in the tree")
        else:
            raise KeyError("Error, data not present in the tree")

    def remove(self, curr_node):
        if (curr_node.left_child is None) and (curr_node.right_child is None):
            if curr_node.parent.left_child is curr_node:
                curr_node.parent.left_child = None
            else:
                curr_node.parent.right_child = None
        elif (curr_node.left_child is not None) and (curr_node.right_child is None):
            if curr_node.parent is not None:
                if curr_node.parent.left_child is curr_node:
                    curr_node.parent.left_child = curr_node.left_child
                else:
                    curr_node.parent.right_child = curr_node.left_child
                curr_node.left_child.parent = curr_node.parent
            else:
                self.root = curr_node.left_child
        elif (curr_node.left_child is None) and (curr_node.right_child is not None):
            if curr_node.parent is not None:
                if curr_node.parent.left_child is curr_node:
                    curr_node.parent.left_child = curr_node.right_child
                else:
                    curr_node.parent.right_child = curr_node.right_child
            else:
                self.root = curr_node.right_child
                curr_node.right_child.parent = None
        else:
            succ_node = self.find_min(curr_node.right_child)
            self.remove(succ_node)

            succ_node.parent = curr_node.parent
            if curr_node.parent is not None:
                if curr_node.parent.left_child is curr_node:
                    curr_node.parent.left_child = succ_node
                else:
                    curr_node.parent.right_child = succ_node
            else:
                self.root = succ_node

            succ_node.left_child = curr_node.left_child
            if curr_node.left_child is not None:
                curr_node.left_child.parent = succ_node

            succ_node.right_child = curr_node.right_child
            if curr_node.right_child is not None:
                curr_node.right_child.parent = succ_node
                