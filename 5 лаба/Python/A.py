class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTreeSearch:
    def __init__(self):
        self.root = None

    def insert(self, x):
        if self.search(x):
            return 'ALREADY'
        else:
            self.root = self._insert(self.root, x)
            return 'DONE'
    def _insert(self, node, x):
        if node is None:
            return Node(x)
        if node.data > x:
            node.left = self._insert(node.left, x)
        elif node.data < x:
            node.right = self._insert(node.right, x)
        return node

    
    def find_max(self):
        if self.root is None:
            return
        return self._max_node(self.root).data
    def _max_node(self, node):
        curr = node
        while curr.right:
            curr = curr.right
        return curr


    def delete(self, x):
        if not self.search(x):
            return 'CANNOT'
        else:
            self.root = self._delete(self.root, x)
            return 'DONE'
    def _delete(self, node, x):
        if node is None:
            return None
        elif node.data > x:
            node.left = self._delete(node.left, x)
        elif node.data < x:
            node.right = self._delete(node.right, x)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            mx_node = self._max_node(node.left)
            node.data = mx_node.data
            node.left = self._delete(node.left, mx_node.data)
        return node

        
    def search(self, x):
        return self._search(self.root, x)
    def _search(self, node, x):
        if node is None:
            return False
        if node.data == x:
            return True
        if node.data > x:
            return self._search(node.left, x)
        return self._search(node.right, x)



    def print_tree(self):
        self._print_tree(self.root, 0)
    def _print_tree(self, node, level):
        if node is None:
            return
        self._print_tree(node.left, level + 1)
        print("." * level + str(node.data))
        self._print_tree(node.right, level + 1)


tree = BinaryTreeSearch()

while True:
    try:
            
        comm = input().split()
        comm1 = comm[0]

        if comm1 == 'ADD':
            print(tree.insert(int(comm[1])))
        elif comm1 == 'DELETE':
            print(tree.delete(int(comm[1])))
        elif comm1 == 'SEARCH':
            if tree.search(int(comm[1])):
                print('YES')
            else:
                print('NO')
        elif comm1 == 'PRINTTREE':
            tree.print_tree()
    except:
        break