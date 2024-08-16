class iArray:
    def __init__(self, capacity, fillValue=None):
        self._items = list()
        for count in range(capacity):
            self._items.append(fillValue)

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __setitem__(self, key, value):
        self._items[key] = value

    def __getitem__(self, item):
        return self._items[item]

    def __iter__(self):
        return iter(self._items)

    def increaseArray(self, a):
        logicalSize = len(([x for x in a if x is not None]))
        physicalSize = len(a)

        if logicalSize == physicalSize:
            temp = iArray(len(a)+1)
            for i in range(logicalSize):
                temp[i] = a[i]
            a = temp
        return a

    def decreaseArray(self, a):
        logicalSize = len(([x for x in a if x is not None]))
        physicalSize = len(a)

        if logicalSize < physicalSize:
            temp = iArray(logicalSize)
            for i in range(logicalSize):
                if a[i] is not None:
                    temp[i] = a[i]
                a = temp
            return a

class iGrid():
    def __init__(self, rows, columns, fillValue = None):
        self._data = iArray(rows)
        for row in range(rows):
            self._data[row] = iArray(columns, fillValue)

    def getRows(self):
        return len(self._data)

    def getColumns(self):
        return len(self._data[0])

    def __getitem__(self, item):
        return self._data[item]

    def __str__(self):
        result = ''
        for row in range(self.getRows()):
            for col in range(self.getColumns()):
                result += str(self._data[row][col]) + ' '
            result += '\n'
        return result

    def sumGrid(self, g):
        sum = 0
        for row in range(g, self.getRows()):
            for column in range(g.getColumns()):
                sum += g[row][column]
        return sum

iMatrix = iGrid(5, 5)
for r in range(iMatrix.getRows()):
    for c in range(iMatrix.getColumns()):
        iMatrix[r][c] = r * c

class aStack(iArray):
    def __init__(self, capacity=5):
        self._items = iArray(capacity)
        self._top = -1
        self._size = 0

    def push(self, newItem):
        if len(self) == len(self._items):
            temp = iArray(2*len(self))
            for i in range(len(self)):
                temp[i] = self._items[i]
                self._items = temp
        self._top += 1
        self._size += 1
        self._items[self._top] = newItem

    def pop(self):
        oldItem = self._items[self._top]
        self._top -= 1
        self._size -= 1
        return oldItem

    def peek(self):
        oldItem = self._items[self._top]
        return oldItem

    def __len__(self):
        return self._size

    def __str__(self):
        result = ' '
        for i in range(len(self)):
            result += str(self._items[i]) + ' '
        return result

class aQueue(iArray):
    def __init__(self, capacity=5):
        self._items =iArray(capacity)
        self._rear = -1
        self._size = 0

    def enque(self, newItem):
        if len(self) == len(self._items):
            temp = iArray(2*len(self))
            for i in range(len(self)):
                temp[i] = self._items[i]
            self._items = temp
            self._rear += 1
            self._size += 1
            self._items[self._rear] = newItem

    def deque(self):
        oldItem = self._items[0]
        for i in range(len(self)-1):
            self._items[i] = self._items[i+1]
        self._rear -= 1
        self._size -= 1
        return oldItem

    def peek(self):
        oldItem = self._items[0]
        return oldItem

    def __len__(self):
        return self._size

    def __str__(self):
        result = ' '
        for i in range(len(self)):
            result += str(self._items[i]) + ' '
        return result


import numpy as np
a = np.array([1, 2, 3])
print(a.shape)

