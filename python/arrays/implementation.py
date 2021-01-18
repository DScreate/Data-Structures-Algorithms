class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length+=1

    def pop(self):
        self.data[self.length] = None
        self.length-=1

    def delete(self, index):
        item = self.data[index]
        self.shiftItems(index)

    def shiftItems(self, index):
        for x in range(index, self.length-1):
            self.data[x] = self.data[x+1]
        self.length-=1

    def __str__(self):
        ret = ''
        for x in range(0, self.length - 1):
            ret += self.data[x].__str__() + ' '
        return ret