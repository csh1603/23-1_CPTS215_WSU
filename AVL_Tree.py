##############################################
# Title: PA3 - AVL Tree
# Author: Seunghyun Cho
# Version: 3.10.6
# Date: Mar 11th, 2023
#
# Description: This program implements AVL Tree
##############################################

# Binary Search Tree Node class for each node
# contains information for data, left child, right child, parent node
class BSTNode:
    def __init__(self, data, left = None, right = None, parent = None):
        self.data = data
        self.left_child = left
        self.right_child = right
        self.parent = parent
        self.balance_factor = 0

# Binary Search Tree class for the structure of tree
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

# AVL Tree class for balancing the tree
# inherit BinarySearchTree
class AVLTree(BinarySearchTree):
    # use Binary Search Tree class's initialization
    def __init__(self):
        super().__init__()

    # method that helps to find whether there is data or not
    def get(self, data):
        if self.root is None:
            return None

        return self._get(data, self.root)

    # method finds data recursively
    def _get(self, data, node):
        # if it founds data, return the data
        if data == node.data:
            return data

        # if the data is less than current node, go to left child
        if data < node.data:
            if node.left_child is None:
                return None
            else:
                self._get(data, node.left_child)

        # if the data is greater than current node, go to right child
        else:
            if node.right_child is None:
                return None
            else:
                self._get(data, node.right_child)

    # method for inputting data
    def put(self, data):
        # if the tree is empty, make the data as root
        if self.root is None:
            self.root = BSTNode(data)
            self.size += 1
        else:
            self._put(data, self.root)

    # method for helping input the data
    def _put(self, data, curr_node):
        # if the data already exists, return
        if data == curr_node.data:
            return

        # if the data is less than current node, go to left child
        if data < curr_node.data:
            # put data if there is no left child to the current node
            if curr_node.left_child is None:
                # make the parent as current node
                curr_node.left_child = BSTNode(data, parent = curr_node)
                self.size += 1
                # since it is pushed into left node increase balance factor by 1
                curr_node.balance_factor += 1
                # make it balanced
                self.update_balance_insert(curr_node)
            # if there is left child to current node, keep track until there is no child node
            else:
                self._put(data, curr_node.left_child)
        # if the data is greater than current node, go to right child
        else:
            # put data if there is no left child to the current node
            if curr_node.right_child is None:
                # make the parent as current node
                curr_node.right_child = BSTNode(data, parent = curr_node)
                self.size += 1
                # since it is pushed into right node decrease balance factor by 1
                curr_node.balance_factor -= 1
                # make it balanced
                self.update_balance_insert(curr_node)
            # if there is right child to current node, keep track until there is no child node
            else:
                self._put(data, curr_node.right_child)

    # method helps to keep balance
    def update_balance_insert(self, node):
        if node.balance_factor == 0:
            return
        # left node's height - right node's height = 1
        elif node.balance_factor == +1:
            if node.parent and node.parent.left_child is node:
                node.parent.balance_factor += 1
                self.update_balance_insert(node.parent)
            elif node.parent and node.parent.right_child is node:
                node.parent.balance_factor -= 1
                self.update_balance_insert(node.parent)

        # left node's height - right node's height = -1
        elif node.balance_factor == -1:
            if node.parent and node.parent.left_child is node:
                node.parent.balance_factor += 1
                self.update_balance_insert(node.parent)
            elif node.parent and node.parent.right_child is node:
                node.parent.balance_factor -= 1
                self.update_balance_insert(node.parent)

        # left node's height - right node's height = -2
        elif node.balance_factor == -2:
            if node.right_child.balance_factor == -1:
                self.rotate_left(node)
            elif node.right_child.balance_factor == 0:
                self.rotate_left(node)
            elif node.right_child.balance_factor == +1:
                self.rotate_right(node.right_child)
                self.rotate_left(node)
            else:
                raise RuntimeError("Unexpected Balance Factor value")

        # left node's height - right node's height = 2
        elif node.balance_factor == +2:
            if node.left_child.balance_factor == +1:
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

    # method rotating data counterclockwise
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

        # update the balance factor
        rot_root.balance_factor = rot_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(rot_root.balance_factor, 0)

    # method rotating data clockwise
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

        # update the balance factor
        rot_root.balance_factor = rot_root.balance_factor - 1 - max(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor - 1 + min(rot_root.balance_factor, 0)

    # method deleting data
    def delete(self, data):
        # if there is only one data in tree
        if self.size == 1 and self.root.data == data:
            self.root = None
            self.size = 0
        # if there are more than 1 data in tree
        elif self.size > 1:
            node_to_remove = self.remove_helper(data, self.root)
            # if it could find the target data
            if node_to_remove is not None:
                self.remove(node_to_remove)
                self.size -= 1
            # if it could not find the target data
            else:
                raise KeyError("Error, data not present in the tree")
        else:
            raise KeyError("Error, data not present in the tree")

    def remove(self, node):
        # if the targeted data is leaf node
         if node.left_child is None and node.right_child is None:
             # leaf node is parent node's left child
             if node.data < node.parent.data:
                 node.parent.balance_factor -= 1
                 node.parent.left_child = None
                 self.update_balance_delete(node.parent)
             # leaf node is parent node's right child
             elif node.data > node.parent.data:
                 node.parent.balance_factor += 1
                 node.parent.right_child = None
                 self.update_balance_delete(node.parent)
                 node.parent = None

         # if the node is internal node with one child
         elif node.left_child is None or node.right_child is None:
             # if the node is not root node
             if node is not self.root:
                 # if the node is parent node's left child
                 if node.data < node.parent.data:
                    node.parent.balance_factor -= 1
                    # if there is right child to targeted node
                    if node.left_child is None:
                        node.parent.left_child = node.right_child
                    # if there is left child to targeted node
                    elif node.right_child is None:
                        node.parent.left_child = node.left_child
                    # keep it is balanced
                    self.update_balance_delete(node.parent)
                    node.parent = None
                 # if the node is parent node's right child
                 elif node.data > node.parent.data:
                    node.parent.balance_factor += 1
                    # if the node has right child
                    if node.left_child is None:
                        node.parent.right_child = node.right_child
                    # if the node has left child
                    elif node.right_child is None:
                        node.parent.right_child = node.left_child
                    # keep it balanced
                    self.update_balance_delete(node.parent)
                    node.parent = None
             # if the node is root node
             else:
                 # make the only child node as a root node
                 if node.left_child is None:
                     self.root = node.right_child
                     self.root.parent = None
                     self.update_balance_delete(self.root)
                 else:
                     self.root = node.left_child
                     self.root.parent = None
                     self.update_balance_delete(self.root)
         # if the targeted node is an internal node with two children nodes
         else:
             curr_node = node
             # find the succssor node (the closest larger value from targeted node)
             succssor_node = node.right_child
             while succssor_node.left_child is not None:
                 succssor_node = succssor_node.left_child
             curr_node.data = succssor_node.data
             self.remove(succssor_node)
             curr_node.balance_factor = curr_node.left_child.balance_factor - curr_node.right_child.balance_factor

    # method find the node
    def remove_helper(self, data, node):
        if data == node.data:
            return node

        if data < node.data:
            if node.left_child is None:
                return None
            else:
                self.remove_helper(data, node.left_child)

        else:
            if node.right_child is None:
                return None
            else:
                self.remove_helper(data, node.right_child)

    # method to keep the tree balanced, same logic as update_balance_insert method
    def update_balance_delete(self, node):
        if node.balance_factor == 0:
            return
        elif node.balance_factor == +1:
            if node.parent and node.parent.left_child is node:
                node.parent.balance_factor += 1
                self.update_balance_insert(node.parent)
            elif node.parent and node.parent.right_child is node:
                node.parent.balance_factor -= 1
                self.update_balance_insert(node.parent)
        elif node.balance_factor == -1:
            if node.parent and node.parent.left_child is node:
                node.parent.balance_factor += 1
                self.update_balance_insert(node.parent)
            elif node.parent and node.parent.right_child is node:
                node.parent.balance_factor -= 1
                self.update_balance_insert(node.parent)
        elif node.balance_factor == -2:
            if node.right_child.balance_factor == -1:
                self.rotate_left(node)
            elif node.right_child.balance_factor == 0:
                self.rotate_left(node)
            elif node.right_child.balance_factor == +1:
                self.rotate_right(node.right_child)
                self.rotate_left(node)
            else:
                raise RuntimeError("Unexpected Balance Factor value")
        elif node.balance_factor == +2:
            if node.left_child.balance_factor == +1:
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

    # method for pre order traversal
    def pre_order_traversal(self):
        if self.root is None:
            print("Empty Tree")
        else:
            self.pre_order_traversal_helper(self.root)
            print()

    # print the node -> left child -> right child
    def pre_order_traversal_helper(self, node):
        # if node is None, return
        if node is None:
            return
        # print the node data and its balance factor
        print(str(node.data) + "(%d)" %(node.balance_factor))
        self.pre_order_traversal_helper(node.left_child)
        self.pre_order_traversal_helper(node.right_child)

    # method for level order traversal
    def level_order_traversal(self):
        if self.root is None:
            print("Empty tree")
        else:
            node_list = [self.root]
            self.level_order_helper(node_list)
            print()

    # print the node by their level
    def level_order_helper(self, node_list):
        if len(node_list) > 0:
            node = node_list.pop(0)
            print(str(node.data) + "(%d)" %(node.balance_factor))
            if node.left_child is not None:
                node_list.append(node.left_child)
            if node.right_child is not None:
                node_list.append(node.right_child)
            self.level_order_helper(node_list)

    # method for post order traversal
    def post_order_traversal(self):
        if self.root is None:
            print("Empty Tree")
        else:
            self.post_order_traversal_helper(self.root)
            print()

    # left child -> right child ->  print the node
    def post_order_traversal_helper(self, node):
        if node is None:
            return
        self.post_order_traversal_helper(node.left_child)
        self.post_order_traversal_helper(node.right_child)
        print(str(node.data) + "(%d)" %(node.balance_factor))

    # method for in order traversal
    def in_order_traversal(self):
        if self.root is None:
            print("Empty Tree")
        else:
            self.in_order_traversal_helper(self.root)
            print()

    # left child -> print the node -> right child
    def in_order_traversal_helper(self, node):
        if node is None:
            return
        self.in_order_traversal_helper(node.left_child)
        print(str(node.data) + "(%d)" %(node.balance_factor))
        self.in_order_traversal_helper(node.right_child)

mytree = AVLTree()

mytree.put(131)
mytree.put(121)
mytree.put(122)
mytree.put(132)
mytree.put(115)
mytree.put(415)
mytree.put(321)
mytree.put(315)
mytree.put(111)

print("pre-order traversal:")
mytree.pre_order_traversal()

print("post-order traversal:")
mytree.post_order_traversal()

print("in-order traversal:")
mytree.in_order_traversal()

print("level-order traversal:")
mytree.level_order_traversal()

print("get method result: ", end=" ")
print(mytree.get(122))
print()

print("deleting 122")
mytree.delete(122)

print("level-order traversal after deleting 122:")
mytree.level_order_traversal()

print("deleting 131")
mytree.delete(131)

print("level-order traversal after deleting 131:")
mytree.level_order_traversal()