class Jar:
    def __init__(self, capacity=12):
        if type(capacity) is int and capacity >= 0:
            self._capacity = capacity
        else:
            raise ValueError("Invalid capacity")
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Too much cookies")
        self._size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Less than 0 cookies")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
