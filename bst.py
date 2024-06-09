class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return True
        return self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
                return True
            else:
                return self._insert(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
                return True
            else:
                return self._insert(node.right, data)
        return False

    def remove(self, data):
        self.root = self._remove(self.root, data)

    def _remove(self, node, data):
        if node is None:
            return node

        if data < node.data:
            node.left = self._remove(node.left, data)
        elif data > node.data:
            node.right = self._remove(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the inorder successor (smallest
            # in the right subtree)
            node.data = self._min_value(node.right)

            # Delete the inorder successor
            node.right = self._remove(node.right, node.data)

        return node

    def _min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.data

    def find(self, data):
        return self._find(self.root, data)

    def _find(self, node, data):
        if node is None:
            return False
        if data < node.data:
            return self._find(node.left, data)
        elif data > node.data:
            return self._find(node.right, data)
        else:
            return True

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        if node is None:
            return []
        return self._inorder(node.left) + [node.data] + self._inorder(node.right)

    def preorder(self):
        return self._preorder(self.root)

    def _preorder(self, node):
        if node is None:
            return []
        return [node.data] + self._preorder(node.left) + self._preorder(node.right)

    def postorder(self):
        return self._postorder(self.root)

    def _postorder(self, node):
        if node is None:
            return []
        return self._postorder(node.left) + self._postorder(node.right) + [node.data]


if __name__ == "__main__":
    b = BST()
    b.insert(56)
    b.insert(34)
    b.insert(70)
    b.insert(5)
    b.insert(1)
    b.insert(42)
    b.insert(40)
    b.insert(52)
    b.insert(62)
    b.insert(57)
    b.insert(89)
    b.insert(90)
    print(b.find(44))
    print(b.find(62))
    b.remove(62)
    print(b.find(62))
    b.insert(44)
    print(b.find(44))
    print("PostOrder:", ' '.join(map(str, b.postorder())))
    print("PreOrder:", ' '.join(map(str, b.preorder())))
    print("InOrder:", ' '.join(map(str, b.inorder())))
