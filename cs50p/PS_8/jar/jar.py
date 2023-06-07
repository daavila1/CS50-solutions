class Jar:
    def __init__(self, capacity = 12, size = 0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n <= self.capacity or (n + self.size) <= self.capacity:
            self.size += n
        else:
            raise ValueError#("Capacity exceeded")

    def withdraw(self, n):
        if self.capacity > n and (self.size - n) >= 0:
            self.size -= n
        else:
            raise ValueError#("Withdraw exceed size")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity <= 0:
            raise ValueError#("Capacity can not be a negative number")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError#("Size is bigger than capacity")
        self._size = size


def main():
    jar = Jar(12, 5)
    jar.deposit(0)
    jar.withdraw(7)
    print(jar)


if __name__ == "__main__":
    main()