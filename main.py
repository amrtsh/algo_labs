class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_tree_balanced(node: BinaryTree) -> bool:
    if node is None:
        return True

    left_height = height_of_tree(node.left)
    right_height = height_of_tree(node.right)

    if abs(left_height - right_height) <= 1 and is_tree_balanced(node.left) and is_tree_balanced(node.right):
        return True

    return False


def height_of_tree(node):
    if node is None:
        return 0

    left_height = height_of_tree(node.left)
    right_height = height_of_tree(node.right)

    return max(left_height, right_height) + 1


if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.left.left.left = BinaryTree(10)
    root.left.left.right = BinaryTree(12)
    root.right.left = BinaryTree(34)
    root.right.right = BinaryTree(36)
    print(is_tree_balanced(root))
