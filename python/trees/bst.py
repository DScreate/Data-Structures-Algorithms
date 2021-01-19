import queue

class BST:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if (self.value is None):
            self.value = value
        elif (value >= self.value):
            if (self.right is None):
                self.right = BST(value)
            else:
                self.right.insert(value)
        else:
            if (self.left is None):
                self.left = BST(value)
            else:
                self.left.insert(value)

    def lookup(self, value):
        if (self.value is None):
            return False
        elif (self.value == value):
            return True
        else:
            return (self.left is not None and self.left.lookup(value)) or (self.right is not None and self.right.lookup(value))

    def remove(self, value):
        if (self.value is None):
            pass
        if (self.right is not None and self.value < value):
            self.right.remove(value)
        if (self.left is not None and self.value > value):
            self.left.remove(value)
        if (self.value == value):
            # No children
            if (self.left is None and self.right is None):
                self.value = None
                del self
            # No right child
            elif (self.right is None):
                self.value = self.left.value
                self.left.remove(self.left.value)
            else:
                self.value = self.right.value
                self.right.remove(self.right.value)
                

    def __str__(self):
        if (self.value is None):
            return ''
        if (self.left is None and self.right is None):
            return str(self.value) 
        else:
            return str(self.value) + ' ->\n ' + str(self.left) + ', ' + str(self.right)

    def BFSQ(self):
        q = queue.SimpleQueue()
        q.put(self)
        while not q.empty():
            cur = q.get()
            if (cur.left is not None):
                q.put(cur.left)
            if (cur.right is not None):
                q.put(cur.right)
            print(cur.value)