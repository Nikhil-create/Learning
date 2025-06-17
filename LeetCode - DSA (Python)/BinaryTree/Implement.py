class Node:
    def __init__(self,value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def insertWithoutRecursion(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        else:
            temp = self.root
            while temp:
                if temp.value == value:
                    return False
                elif temp.value > value:
                    if temp.left is None:
                        temp.left = new_node
                        return True
                    temp = temp.left 
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return True
                    temp = temp.right

    def containWithoutRecursion(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp:
            if temp.value == value:
                return True
            elif temp.value > value:
                temp = temp.left
            else:
                temp = temp.right
        return False



# BST without Recursion
tree_1 = BinaryTree()
tree_1.insertWithoutRecursion(5)
tree_1.insertWithoutRecursion(4)
tree_1.insertWithoutRecursion(6)
tree_1.insertWithoutRecursion(3)
tree_1.insertWithoutRecursion(2)


print(f"{tree_1.root.value}")
print(f"L - {tree_1.root.left.value}    R - {tree_1.root.right.value}")
print(f"L - {tree_1.root.left.left.value}")
print(f"L - {tree_1.root.left.left.left.value}")

print(tree_1.containWithoutRecursion(9))
print(tree_1.containWithoutRecursion(3))
