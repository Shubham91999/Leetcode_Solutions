class LRUCache:

    def __init__(self, capacity):
        self.cache = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        # checking if key present
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:  # if found, return value present at the key
                temp = self.cache.pop(i)
                self.cache.append(temp)
                return temp[1]
        return -1  # key not present, return -1

    def put(self, key: int, value: int) -> None:
        # Checking if key already present
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                # key found in cache
                temp = self.cache.pop(i)  # Removed the cache present at key
                temp[1] = value  # Updated the value
                self.cache.append(temp)  # Appended to make it most recently used
                return

        # Key not found
        if len(self.cache) == self.capacity:  # Checking the length of cache list
            self.cache.pop(0)  # if already at capacity, pop LRU cache
        self.cache.append([key, value])  # append new pair as MRU
