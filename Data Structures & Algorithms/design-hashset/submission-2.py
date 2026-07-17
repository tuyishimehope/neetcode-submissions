class MyHashSet:

    def __init__(self):
        self.hashset = [[] for _ in range(100)]

    def add(self, key: int) -> None:
        bucket = key % 100
        for el in self.hashset[bucket]:
            if el == key:
                return
        self.hashset[bucket].append(key)

    def remove(self, key: int) -> None:
        bucket = key % 100
        for el in self.hashset[bucket]:
            if el == key:
                self.hashset[bucket].remove(key)
                return

    def contains(self, key: int) -> bool:
        bucket = key % 100
        for el in self.hashset[bucket]:
            if el == key:
                return True
        return False


