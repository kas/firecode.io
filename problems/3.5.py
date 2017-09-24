# 3.5 Find the Minimum BST Node

class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node

    def find_min(self, root):
        if not root:
            return TreeNode(None)

        while root.left_child:
            root = root.left_child

        return TreeNode(root.data)
