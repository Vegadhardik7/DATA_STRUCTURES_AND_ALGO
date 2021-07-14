from exceptions import Empty
class ArrayDeque:
    def __init__(self):
        self._data = []
        self._front = 0

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def first(self):
        if self.is_empty():
            raise Empty("Deque is Empty")
        return self._data[self._front]

    def last(self):
        if self.is_empty():
            raise Empty("Deque is Empty")
        return self._data[-1]

    def add_first(self,e):
        self._data.insert(self._front,e)

    def add_last(self,e):
        self._data.append(e)

    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is Empty")
        value = self._data.pop(self._front)
        return value

    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is Empty")
        value = self._data.pop()
        return value

d = ArrayDeque()
d.add_last(10)
d.add_last(20)
d.add_last(30)
d.add_last(40)
d.add_last(50)
print('Deque:',d._data)

print("First Element:",d.first())
print("Last Element:",d.last())

print("Delete First:",d.delete_first())
print('Deque:',d._data)

print("Delete Last:",d.delete_last())
print('Deque:',d._data)

d.add_first(5)
print('Deque:',d._data)

d.add_last(100)
print('Deque:',d._data)

print("Length:",len(d))