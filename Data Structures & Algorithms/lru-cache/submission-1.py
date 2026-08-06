class Node:
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.prev = None
        self.nex = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.maxCap = capacity
        self.mru = Node(0, 0)
        self.lru = Node(0, 0)
        self.lru.nex, self.mru.prev = self.mru, self.lru

    def remove(self, node):
        prev, nxt = node.prev, node.nex
        prev.nex, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.mru.prev, self.mru
        prev.nex = nxt.prev = node
        node.nex, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.maxCap:
            lru = self.lru.nex
            self.remove(lru)
            del self.cache[lru.key]
            



