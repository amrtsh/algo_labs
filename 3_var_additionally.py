class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binary_tree_diameter(node: BinaryTree) -> int:
    def height_of_tree(node):
        if node is None:
            return 0

        left_height = height_of_tree(node.left)
        right_height = height_of_tree(node.right)

        return max(left_height, right_height) + 1

    def diameter(node):
        if node is None:
            return 0

        left_diameter = diameter(node.left)
        right_diameter = diameter(node.right)

        left_height = height_of_tree(node.left)
        right_height = height_of_tree(node.right)

        curr_diameter = max(left_diameter, right_diameter, left_height + right_height)

        return curr_diameter

    return diameter(node)


if __name__ == '__main__':
    # root = BinaryTree(1)
    # root.left = BinaryTree(3)
    # root.right = BinaryTree(2)
    # root.left.left = BinaryTree(7)
    # root.left.right = BinaryTree(4)
    # root.left.left.left = BinaryTree(8)
    # root.left.left.left.left = BinaryTree(9)
    # root.left.right.right = BinaryTree(5)
    # root.left.right.right.right = BinaryTree(6)
    root = BinaryTree(50)
    root.left = BinaryTree(17)
    root.right = BinaryTree(72)
    root.right.right = BinaryTree(76)
    root.left.left = BinaryTree(12)
    root.left.left.left = BinaryTree(9)
    root.left.left.right = BinaryTree(14)
    root.left.right = BinaryTree(23)
    root.left.right.left = BinaryTree(19)
    root.right.left = BinaryTree(54)
    root.right.left.right = BinaryTree(67)

    print(binary_tree_diameter(root))
