from array import * 
# import queueArray as QArr

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def Insert(root):
    n = int(input("Enter data:: "))
    root  = Node(n)
    
    if (n == -1):
        return None

    print("Enter data for inserting in left of ", root.data)
    root.left = Insert(root.left)
    print("Enter data for inserting in right of ", root.data)
    root.right = Insert(root.right)

    return root


def bstInsert(root,n):
    if root is None:
        return Node(n)
    
    if root.data > n:
        root.left = bstInsert(root.left,n)
    else:
        root.right = bstInsert(root.right,n)

    return root

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end=", ")
        inOrder(root.right)

def preOrder(root):
    if root:
        print(root.data, end=", ")
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=", ")
    
def BSTree():
    # treeArray = array('i', [1, 3, 5, 7, 11, 17, -1, -1, -1, -1, -1, -1, -1])
    bst = array('i', [10,1, 3, 5, 7, 11, 17,-1, -1, -1, -1, -1, -1, -1])
    root = None
    # root  = Node(5)
    for values in bst:
        if ( values != -1):
            root = bstInsert(root,values)
        # print(bst[i], end=", ")
    return root
def levelOrder(root):
    if root is None:
        return
    
    queue = []
    queue.append(root)

    while len(queue) > 0:
        # Count the number of nodes at the current level
        level_nodes = len(queue)

        # Dequeue all nodes at the current level and enqueue their children
        for _ in range(level_nodes):
            node = queue.pop(0)
            print(node.data, end=" ")

            if node.left is not None:
                queue.append(node.left)
            
            if node.right is not None:
                queue.append(node.right)
        
        # Print a newline to separate levels
        print()

def printTree(root):
    if root is None:
        return

    # Use a queue to perform level-order traversal
    queue = [(root, 0)]

    # Dictionary to store nodes at each level
    level_nodes = {}

    while queue:
        node, level = queue.pop(0)

        # Add the node to the dictionary based on its level
        if level in level_nodes:
            level_nodes[level].append(node)
        else:
            level_nodes[level] = [node]

        # Enqueue the left and right children of the current node
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    # Print nodes level by level with indentation
    for level, nodes in level_nodes.items():
        print("Level", level, ": ", end="")
        for node in nodes:
            print(node.data, end=" ")
        print()

root  = BSTree()
print("inOeder")
inOrder(root)
print()
print("preOeder")
preOrder(root)
print()
print("PostOeder")
postOrder(root)

print()
print("levelOrder")
printTree(root)


# root = Insert(root)
