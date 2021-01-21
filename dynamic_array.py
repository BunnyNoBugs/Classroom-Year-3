import numpy as np


class DynamicArray:
    def __init__(self, items: tuple = None):
        if items:
            self._items = np.array(items)
            self._length = len(self._items)
        else:
            self._items = None
            self._length = 0

    def append(self, elem):
        if self._length == 0:
            self._items = np.empty(2)
            self._items[0] = elem
        else:
            if self._length + 1 > len(self._items):
                dumped_items = self._items
                self._items = np.empty(self._length * 2)
                self._items[:self._length] = dumped_items
                self._items[self._length] = elem
            else:
                self._items[self._length] = elem
        self._length += 1
        print(self._items)

    def __getitem__(self, key):
        if key > self._length - 1:
            raise KeyError(key)
        else:
            return self._items[key]

    def __setitem__(self, key, value):
        if key > self._length - 1:
            raise KeyError(key)
        else:
            self._items[key] = value

    def __iter__(self):
        self._iter_idx = -1

        return self

    def __next__(self):
        if self._iter_idx > self._length - 2:
            raise StopIteration
        self._iter_idx += 1

        return self._items[self._iter_idx]

    def __str__(self):
        str_repr = '['
        for i in a:
            str_repr += str(i)
            str_repr += ', '
        str_repr = str_repr.rstrip(', ')
        str_repr += ']'

        return str_repr


a = DynamicArray((11, 10))
print(a[0])
for i in a:
    print(i)
a[0] = 10
print(a[0])
print(a)
