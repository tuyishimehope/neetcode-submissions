class MyHashSet:

    def __init__(self):
        self.arr = []
        

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.arr.append(key)

    def remove(self, key: int) -> None:
        while key in self.arr:
            self.arr.remove(key)

    def contains(self, key: int) -> bool:
        for el in self.arr:
            if key == el:
                return True
        return False
