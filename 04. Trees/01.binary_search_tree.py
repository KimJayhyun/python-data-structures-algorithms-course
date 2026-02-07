class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)

        if self.root is None:
            self.root = node
            return True

        current = self.root
        while True:
            if current.value > value:
                if current.left is None:
                    current.left = node
                    return True

                current = current.left

            elif current.value < value:
                if current.right is None:
                    current.right = node
                    return True

                current = current.right

            else:
                return False

    def contains(self, value):
        # if self.root is None:
        if not self.root:
            return False

        current = self.root

        # while current is not None:
        while current:
            if current.value > value:
                current = current.left
            elif current.value < value:
                current = current.right
            else:
                return True
        else:
            return False


my_tree = BinarySearchTree()

print(my_tree.root)


"""
    EXPECTED OUTPUT:
    ----------------
    None

"""


my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

"""
    THE LINES ABOVE CREATE THIS TREE:
                 2
                / \
               1   3
"""


print("Root:", my_tree.root.value)
print("Root->Left:", my_tree.root.left.value)
print("Root->Right:", my_tree.root.right.value)


"""
    EXPECTED OUTPUT:
    ----------------
    Root: 2
    Root->Left: 1
    Root->Right: 3

"""


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print("BST Contains 27:")
print(my_tree.contains(27))

print("\nBST Contains 17:")
print(my_tree.contains(17))


"""
    EXPECTED OUTPUT:
    ----------------
    BST Contains 27:
    True

    BST Contains 17:
    False

"""
