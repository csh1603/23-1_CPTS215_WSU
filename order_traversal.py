# class for each node in Binary Search Tree
class BSTNode:
    def __init__(self, data, left_child = None, right_child = None, parent = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
    def put(self, data):
        if self.root is None:
            self.root = BSTNode(data)
            self.size += 1
        else:
            self._put(data, self.root)
    def _put(self, data, curr_node):
        if data == curr_node.data:
            return
        if data < curr_node.data:
            if curr_node.left_child is None:
                curr_node.left_child = BSTNode(data, parent = curr_node)
                self.size += 1
            else:
                self._put(data, curr_node.left_child)
        else:
            if curr_node.right_child is None:
                curr_node.right_child = BSTNode(data, parent = curr_node)
                self.size += 1
            else:
                self._put(data, curr_node.right_child)

    def post_order_traversal(self):
        if self.root is None:
            print("Empty Tree")
        else:
            self.post_order_traversal_helper(self.root)
            print()

    def post_order_traversal_helper(self, node):
        if node is None:
            return
        self.post_order_traversal_helper(node.left_child)
        self.post_order_traversal_helper(node.right_child)
        print(node.data, end = " ")

    def pre_order_traversal(self):
        if self.root is None:
            print("Empty Tree")
        else:
            self.pre_order_traversal_helper(self.root)
            print()

    def pre_order_traversal_helper(self, node):
        if node is None:
            return
        print(node.data, end = " ")
        self.pre_order_traversal_helper(node.left_child)
        self.pre_order_traversal_helper(node.right_child)


    def in_order_traversal(self):
        if self.root is None:
            print("Empty Tree")
        else:
            self.in_order_traversal_helper(self.root)
            print()

    def in_order_traversal_helper(self, node):
        if node is None:
            return
        self.in_order_traversal_helper(node.left_child)
        print(node.data, end = " ")
        self.in_order_traversal_helper(node.right_child)
myTree = BinarySearchTree()

myTree.put("language")
myTree.put("complied")
myTree.put("C")
myTree.put("Java")
myTree.put("interpreted")
myTree.put("python")
myTree.put("scheme")

myTree.post_order_traversal()