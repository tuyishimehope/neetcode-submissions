class MyHashMap:
    def __init__(self):
        self.hashmap = [[] for _ in range(100)]
    
    def _bucket_index(self, key):
        return key % len(self.hashmap)

    def put(self, key: int, value: int) -> None:
        bucket = self._bucket_index(key)
        for el in self.hashmap[bucket]:
            if el[0] == key:
                el[1] = value
                return
        self.hashmap[bucket].append([key, value])

    def get(self, key: int) -> int:
        bucket = self._bucket_index(key)
        for el in self.hashmap[bucket]:
            if el[0] == key:
                return el[1]
        return -1

    def remove(self, key: int) -> None:
        bucket = self._bucket_index(key)
        for i, el in enumerate(self.hashmap[bucket]):
            if el[0] == key:
                self.hashmap[bucket].pop(i)
                return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
