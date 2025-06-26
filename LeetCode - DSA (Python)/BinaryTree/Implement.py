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
    
    def __r_contains(self, curr_node,value):
        if curr_node is None:
            return False
        if value == curr_node.value:
            return True
        elif value < curr_node.value:
            return self.__r_contains(curr_node.left,value)
        else:
            return self.__r_contains(curr_node.right,value)

    def r_contains(self,value):
        return self.__r_contains(self.root,value)
    
    def __r_insert(self,curr_node,value):

        if curr_node == None:
            return Node(value)
        if value < curr_node.value:
            curr_node.left = self.__r_insert(curr_node.left,value)
        if value > curr_node.value:
            curr_node.right = self.__r_insert(curr_node.right,value)
        return curr_node
    
    def __delete_node(self,curr_node,value):
        if curr_node == None:
            return None
        if value < curr_node.value:
            curr_node.left = self.__delete_node(curr_node.left,value)
        elif value > curr_node.value:
            curr_node.right = self.__delete_node(curr_node.right,value)
        else:
            if curr_node.left == None and curr_node.right == None:
                return None
            elif curr_node.left == None:
                curr_node = curr_node.right
            elif curr_node.right == None:
                curr_node = curr_node.left 
            else:
                subtree_min = self.min_value(curr_node)
                curr_node.value = subtree_min
                curr_node.right = self.__delete_node(curr_node.right,subtree_min)


        return curr_node
    
    def min_value(self,curr_node):
        while curr_node.left is not None:
            curr_node= curr_node.left
        return curr_node.value



    def r_delete_node(self,value):
        self.__delete_node(self.root,value)

    def r_insert(self,value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root,value)


    #Breath First Search
    def BFS(self):
        curr_node = self.root
        queue = []
        results = []
        queue.append(curr_node)
        while len(queue)>0:
            curr_node = queue.pop(0)
            results.append(curr_node.value)
            if curr_node.left is not None:
                queue.append(curr_node.left)
            if curr_node.right is not None:
                queue.append(curr_node.right)
        return results



# BST without Recursion
tree_1 = BinaryTree()
tree_1.insertWithoutRecursion(47)
tree_1.insertWithoutRecursion(21)
tree_1.insertWithoutRecursion(57)
tree_1.insertWithoutRecursion(18)
tree_1.insertWithoutRecursion(2)

tree_1.r_insert(49)

print("Min Value ", tree_1.min_value(tree_1.root))
print("Min Value ",tree_1.min_value(tree_1.root.right))


print(f"{tree_1.root.value}")
print(f"L - {tree_1.root.left.value}    R - {tree_1.root.right.value}")
print(f"L - {tree_1.root.left.left.value} R - {tree_1.root.right.left.value}")
print(f"L - {tree_1.root.left.left.left.value}")

print(tree_1.containWithoutRecursion(9))
print(tree_1.containWithoutRecursion(3))

#Recursion
print(tree_1.r_contains(3))
print(tree_1.r_contains(16))
print(tree_1.r_contains(6))

print(tree_1.BFS())

