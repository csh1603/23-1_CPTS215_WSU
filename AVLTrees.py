class BSTNode:
    def __init__(self, data, left = None, right = None, parent = None):
        self.data = data
        self.left_child = left
        self.right_child = right
        self.parent = parent
        self.balance_factor = 0

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
        print(node.data, end = "")
        self.pre_order_traversal_helper(node.left_child)
        self.pre_order_traversal_helper(node.right_child)

    def level_order_traversal(self):
        if self.root is None:
            print("Empty tree")
        else:
            node_list = [self.root]
            self.level_order_helper(node_list)
            print()

    def level_order_helper(self, node_list):
        if len(node_list) > 0:
            node = node_list.pop(0)
            print(node.data, end = "")
            if node.left_child is not None:
                node_list.append(node.left_child)
            if node.right_child is not None:
                node_list.append(node.right_child)

            self.level_order_helper(node_list)

    def get(self, data):
        if self.root is None:
            return None
        else:
            node = self._get(data, self.root)
            if node is not None:
                return node.data
            else:
                return None

    def _get(self, data, curr_node):
        if curr_node is None:
            return None
        else:
            if data == curr_node.data:
                return curr_node
            if data < curr_node.data:
                return self._get(data, curr_node.left_child)
            else:
                return self._get(data, curr_node.right_child)

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

    def delete(self, data):
        if self.size == 1 and self.root.data == data:
            self.root = None
            self.size = 0
        elif self.size > 1:
            node_to_remove = self._get(data, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
        else:
            raise KeyError('Error, data not in tree')

    def remove(self, curr_node):
        if (curr_node.left_child is None) and (curr_node.right_child is None):
            if curr_node is curr_node.parent.left_child:
                curr_node.parent.left_child = None
            else:
                curr_node.parent.right_child = None

        elif (curr_node.left_child is not None and curr_node.right_child is None):
            if curr_node.parent is not None:
                if curr_node.parent.left_child is curr_node:
                    curr_node.parent.left_child = curr_node.left_child
                else:
                    curr_node.parent.right_child = curr_node.right_child
                curr_node.left_child.parent = curr_node.parent
            else:
                self.root = curr_node.left_child
                curr_node.left_child.parent = None
        elif (curr_node.left_child is None and curr_node.right_child is not None):
            if curr_node.parent is not None:
                if curr_node.parent.left_child is curr_node:
                    curr_node.parent.left_child = curr_node.right_child
                else:
                    curr_node.paren.right_child = curr_node.right_child
                curr_node.right_child.parent = curr_node.parent
            else:
                self.root = curr_node.right_child
                curr_node.right_child.parent = None
        else:
            succ_node = self.find_min_child(curr_node.right_child)
            self.remove(succ_node)

            succ_node.parent = curr_node.parent
            if curr_node.parent:
                if curr_node.parent.left_child is curr_node:
                    curr_node.parent.left_child = succ_node
                else:
                    curr_node.parent.right_child = succ_node
            else:
                self.root = succ_node
            succ_node.left_child = curr_node.left_child
            if curr_node.left_child:
                curr_node.left_child.parent = succ_node
            succ_node.right_child = curr_node.right_child
            if curr_node.right_child:
                curr_node.right_child.parent = succ_node

    def find_min_child(self, curr_node):
        if curr_node.left_child is None:
            return curr_node
        else:
            return self.find_min_child(curr_node.left_child)

class AVLTree(BinarySearchTree):
    def __init__(self):
        super.__init__()

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
                curr_node.balance_factor += 1
                self.update_balance_insert(curr_node)
            else:
                self._put(data, curr_node.left_child)
        else:
            if curr_node.right_child is None:
                curr_node.right_child = BSTNode(data, parent = curr_node)
                self.size += 1
                curr_node.balance_factor -= 1
                self.update_balance_insert(curr_node)
            else:
                self._put(data, curr_node.right_child)

    def update_balance_insert(self, node):
        if node.balance_factor == 0:
            return
        elif node.balance_factor == 1:
            if node.parent and node.parent.left_child is node:
                node.parent.balance_factor += 1
                self.update_balance_insert(node.parent)
            elif node.parent and node.parent.right_child is node:
                node.parent.balance_factor -= 1
                self.update_balance_insert(node.parent)
        elif node.balance_factor == -1:
            if node.parent and node.parent.left_child is node:
                node.parent.balance_factor += 1
                self.update_balance_insert(node.parnet)
            elif node.parent and node.parent.right_child is node:
                node.parent.balance_factor -= 1
                self.update_balance_insert(node.parent)
        elif node.balance_factor == -2:
            if node.right_child.balance_factor == -1:
                self.rotate_left(node)
            elif node.right_child.balance_factor == 0:
                self.rotate_left(node)
            elif node.right_child.balance_factor == 1:
                self.rotate_right(node.right_child)
                self.rotate_left(node)
            else:
                raise RuntimeError("Unexpected Balance Factor value")
        elif node.balance_factor == 2:
            if node.left_child.balance_factor == 1:
                self.rotate_right(node)
            elif node.left_child.balance_factor == 0:
                self.rotate_right(node)
            elif node.left_child.balance_factor == -1:
                self.rotate_left(node.left_child)
                self.rotate_right(node)
            else:
                raise RuntimeError("Unexpected Balance Factor value")
        else:
            raise RuntimeError("Unexpected Balance Factor value")

    def rotate_left(self, rot_root):
        new_root = rot_root.right_child

        rot_root.right_child = new_root.left_child
        if new_root.left_child != None:
            new_root.left_child.parent = rot_root

        new_root.parent = rot_root.parent
        if rot_root.parent is None:
            self.root = new_root
        else:
            if rot_root.parent.left_child is rot_root:
                rot_root.parent.left_child = new_root
            else:
                rot_root.parent.right_child = new_root

        new_root.left_child = rot_root
        rot_root.parent = new_root

        rot_root.balance_factor = rot_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(rot_root.balance_factor, 0)

    def rotate_right(self, rot_root):
        new_root = rot_root.left_child

        rot_root.left_child = new_root.right_child
        if new_root.right_child != None:
            new_root.right_child.parent = rot_root

        new_root.parent = rot_root.parent
        if rot_root.parent is None:
            self.root = new_root
        else:
            if rot_root.parent.right_child is rot_root:
                rot_root.parent.right_child = new_root
            else:
                rot_root.parent.left_child = new_root

        new_root.right_child = rot_root
        rot_root.parent = new_root

        rot_root.balance_factor = rot_root.balance_factor - 1 - max(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor - 1 + min(rot_root.balance_factor, 0)

    def delete(self, data):
        if self.size == 1 and self.root.data == data:
            self.root = None
            self.size = 0
        elif self.size > 1:
            node_to_remove = self._get(data, self.root)
            if node_to_remove is not None:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError("Error, data not present in the tree")
        else:
            raise KeyError("Error, data not present in the tree")

    def remove(self, curr_node):
        pass

    def update_balance_delete(self, node):
        pass

    def pre_order_traversal(self):
        if self.root is None:
            print("Empty tree")
        else:
            self.pre_order_traversal_helper(self.root)
            print()

    def pre_order_traversal_helper(self, node):
        if node is None:
            return
        print(str(node.data) + "(%d)" %(node.balance_factor))
        self.pre_order_traversal_helper(node.left_child)
        self.pre_order_traversal_helper(node.right_child)

    def level_order_traversal(self):
        if self.root is None:
            print("Empty Tree")
        else:
            node_list = [self.root]
            self.level_order_helper(node_list)
            print()

    def level_order_helper(self, node_list):
        if len(node_list) > 0:
            node = node_list.pop(0)
            print(str(node.data) + "(%d)" %(node.balance_factor))
            if node.left_child is not None:
                node_list.append(node.left_child)
            if node.left_child is not None:
                node_list.append(node.right_child)

            self.level_order_helper(node_list)