from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)  # Mark as recently used
            return self.cache[key]
        return -1  # Key not found

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)  # Mark as recently used
        self.cache[key] = value  # Insert/Update key-value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove LRU (first element)

# Running the given input sequence
commands = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
inputs = [[2], [1,1], [2,2], [1], [3,3], [2], [4,4], [1], [3], [4]]

lru = None
output = []

for i, cmd in enumerate(commands):
    if cmd == "LRUCache":
        lru = LRUCache(*inputs[i])  # Initialize LRU Cache
        output.append(None)
    elif cmd == "put":
        lru.put(*inputs[i])  # Perform put operation
        output.append(None)
    elif cmd == "get":
        output.append(lru.get(*inputs[i]))  # Perform get operation

print(output)  # Expected output: [None, None, None, 1, None, -1, None, -1, 3, 4]
