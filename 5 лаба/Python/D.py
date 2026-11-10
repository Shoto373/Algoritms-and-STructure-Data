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
            return 
        else:
            self.root = self._insert(self.root, x)
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
    
    def find_max2(self):
        if self.root is None:
            return
        return self._max2_node(self.root).data
    def _max2_node(self, node):
        
        curr = node
        pred = None

        while curr.right:
            pred = curr
            curr = curr.right
        
        if curr.left:
            curr = curr.left
            while curr.right:
                curr = curr.right
            return curr
        
        return pred        

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

    def order_up(self):
        self._order_up(self.root, 0)

    def _order_up(self, node):
        if node is None:
            return []
        return self._order_up(node.left) + [node.data] + self._order_up(node.right)
    

    def size(self):
        return self._size(self.root)
    def _size(self, node):
        if node is None:
            return 0 
        return 1 + self._size(node.left) + self._size(node.right)

tree = BinaryTreeSearch()   

x = input().split()[:-1]
for i in x:
    tree.insert(int(i))
print(tree.find_max2())