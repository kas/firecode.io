# 2.3 Count the Leaves!

class BinaryTree:
    def __init__(self, root_node = None):
            self.root = root_node

    def number_of_leaves(self, root):
        if not root:
            return 0

        if not root.left_child and not root.right_child:
            return 1

        return self.number_of_leaves(root.left_child) + self.number_of_leaves(root.right_child)
