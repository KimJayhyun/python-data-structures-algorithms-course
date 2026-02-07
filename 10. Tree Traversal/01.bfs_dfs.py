class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def BFS(self):
        current_node = self.root
        queue = [current_node]
        result = []

        while len(queue) > 0:
            current_node = queue.pop(0)

            if not current_node.left is None:
                queue.append(current_node.left)

            if not current_node.right is None:
                queue.append(current_node.right)

            result.append(current_node.value)

        return result

    def dfs_pre_order(self):
        result = []

        def traverse(node):
            result.append(node.value)

            if not node.left is None:
                traverse(node.left)

            if not node.right is None:
                traverse(node.right)

        traverse(self.root)

        return result

    def dfs_post_order(self):
        result = []

        def traverse(node):
            if not node.left is None:
                traverse(node.left)

            if not node.right is None:
                traverse(node.right)

            result.append(node.value)

        traverse(self.root)

        return result

    def dfs_in_order(self):
        result = []

        def traverse(node):
            if not node.left is None:
                traverse(node.left)

            result.append(node.value)

            if not node.right is None:
                traverse(node.right)

        traverse(self.root)

        return result


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.BFS())


"""
    EXPECTED OUTPUT:
    ----------------
    [47, 21, 76, 18, 27, 52, 82]

 """

print("===")
print(my_tree.dfs_pre_order())


"""
    EXPECTED OUTPUT:
    ----------------
    [47, 21, 18, 27, 76, 52, 82]

 """

print("===")
print(my_tree.dfs_post_order())


"""
    EXPECTED OUTPUT:
    ----------------
    [18, 27, 21, 52, 82, 76, 47]

 """

print("===")
print(my_tree.dfs_in_order())


"""
    EXPECTED OUTPUT:
    ----------------
    [18, 21, 27, 47, 52, 76, 82]

 """
