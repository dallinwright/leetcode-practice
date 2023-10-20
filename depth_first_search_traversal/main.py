# Definition for a binary tree node. Note, this is unbalances.
class Node:
    def __init__(self, value=0, depth=0, left=None, right=None):
        self.depth: int = depth
        self.value: int = value
        self.left: Node = left
        self.right: Node = right

    def insert(self, value: int, depth=0):
        depth += 1

        # Compare the new value with the parent node
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value, depth=depth)
                else:
                    self.left.insert(value, depth=depth)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value, depth=depth)
                else:
                    self.right.insert(value, depth=depth)
        else:
            self.value = value

    def depth_first_search(self, value):
        message = "-" * self.depth
        message += str(self.value)
        print(message)

        if value < self.value:
            if self.left is None:
                return None
            return self.left.depth_first_search(value)
        elif value > self.value:
            if self.right is None:
                return None
            return self.right.depth_first_search(value)

    def print_tree(self):
        if self.left:
            self.left.print_tree()

        if self.right:
            self.right.print_tree()

        print(self.value)


def test_dfs():
    tree = Node(1)
    tree.insert(2)
    tree.insert(9)
    tree.insert(3)
    tree.insert(5)
    tree.insert(4)

    result = tree.depth_first_search(4)
    print(tree.print_tree())
    print(f"depth: {result.depth} result: {result.value}")
    print("done")
