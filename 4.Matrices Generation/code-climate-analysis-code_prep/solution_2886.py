class BinaryTree:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

    def set_root(self, key):
        self.key = key

    def insert_left(self, new_node):
        self.left = new_node

    def insert_right(self, new_node):
        self.right = new_node

    def search(self, key):
        if self.key == key:
            return self
        if self.left is not None:
            temp =  self.left.search(key)
            if temp is not None:
                return temp
        if self.right is not None:
            temp =  self.right.search(key)
            return temp
        return None

    def mirror_copy(self):
        mirror = BinaryTree(self.key)
        if self.right is not None:
            mirror.left = self.right.mirror_copy()
        if self.left is not None:
            mirror.right = self.left.mirror_copy()
        return mirror

    def bfs(self):
        queue = [self]
        while queue != []:
            popped = queue.pop(0)
            if popped.left is not None:
                queue.append(popped.left)
            if popped.right is not None:
                queue.append(popped.right)
            print(popped.key, end=' ')


btree = None

print('Menu (this assumes no duplicate keys)')
print('insert <data> at root')
print('insert <data> left of <data>')
print('insert <data> right of <data>')
print('mirror')
print('quit')

while True:
    do = input('What would you like to do? ').split()

    operation = do[0].strip().lower()
    if operation == 'insert':
        data = int(do[1])
        new_node = BinaryTree(data)
        suboperation = do[2].strip().lower() 
        if suboperation == 'at':
                btree = new_node
        else:
            position = do[4].strip().lower()
            key = int(position)
            ref_node = None
            if btree is not None:
                ref_node = btree.search(key)
            if ref_node is None:
                print('No such key.')
                continue
            if suboperation == 'left':
                ref_node.insert_left(new_node)
            elif suboperation == 'right':
                ref_node.insert_right(new_node)

    elif operation == 'mirror':
        if btree is not None:
            print('Creating mirror copy...')
            mirror = btree.mirror_copy()
            print('BFS traversal of original tree: ')
            btree.bfs()
            print()
            print('BFS traversal of mirror: ')
            mirror.bfs()
            print()

    elif operation == 'quit':
        break