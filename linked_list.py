import typing as tp


class Node:
    def __init__(self, value: int = None, next: 'Node' = None):
        self._value = value
        self._next = next


class LinkedList:
    def __init__(self, values: tp.Union[int, tuple] = None):
        if isinstance(values, int):
            self._head = Node(values)
            self._tail = self._head
            self._length = 1
        elif isinstance(values, tuple):
            self._head = Node(values[0])
            self._tail = self._head
            self._length = 1
            if len(values) > 1:
                for i in values[1:]:
                    self._tail._next = Node(i)
                    self._tail = self._tail._next
                    self._length += 1
        else:
            raise TypeError(f'Wrong argument type: {type(values)}')

    def __iter__(self):
        curr = self._head
        while curr is not None:
            yield curr._value
            curr = curr._next

    def __len__(self):
        return self._length

    def append(self, value):
        self._tail._next = Node(value)
        self._tail = self._tail._next
        self._length += 1

    def __str__(self):
        str_repr = '['
        for i in self:
            str_repr += str(i)
            str_repr += ', '
        str_repr = str_repr.rstrip(', ')
        str_repr += ']'

        return str_repr

    def __getitem__(self, key):
        if key > self._length - 1:
            raise KeyError(key)
        else:
            count = 0
            for i in self:
                if count == key:
                    return i
                count += 1

    def __setitem__(self, key, value):
        if key > self._length - 1:
            raise KeyError(key)
        else:
            count = 0
            curr = self._head
            while count != key:
                count += 1
                curr = curr._next
            curr._value = value


ll = LinkedList((9, 10))
for i in ll:
    print(i)
print(len(ll))
ll.append(11)
print(ll)
print(ll[2])
ll[0] = 8
print(ll)
