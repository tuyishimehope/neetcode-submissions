class MyHashSet:

    def __init__(self):
        self.arr = [0] * 1_000_000
        

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.arr[key] = 1

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.arr[key] = 0

    def contains(self, key: int) -> bool:
        if self.arr[key]:
            return True
        return False
