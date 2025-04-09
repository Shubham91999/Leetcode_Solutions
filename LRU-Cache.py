# 1. Brute Force
# class LRUCache:

#     def __init__(self, capacity):
#         self.cache = []
#         self.capacity = capacity

#     def get(self, key: int) -> int:
#         # checking if key present
#         for i in range(len(self.cache)):
#             if self.cache[i][0] == key:  # if found, return value present at the key
#                 temp = self.cache.pop(i)
#                 self.cache.append(temp)
#                 return temp[1]
#         return -1  # key not present, return -1

#     def put(self, key: int, value: int) -> None:
#         # Checking if key already present
#         for i in range(len(self.cache)):
#             if self.cache[i][0] == key:
#                 # key found in cache
#                 temp = self.cache.pop(i)  # Removed the cache present at key
#                 temp[1] = value  # Updated the value
#                 self.cache.append(temp)  # Appended to make it most recently used
#                 return

#         # Key not found
#         if len(self.cache) == self.capacity:  # Checking the length of cache list
#             self.cache.pop(0)  # if already at capacity, pop LRU cache
#         self.cache.append([key, value])  # append new pair as MRU

# 2. Doubly Linked List
# Doubly Linked List Node
# class Node:
#     def __init__(self, key, val):
#         self.key, self.value = key, val  # to store key value pairs 
#         self.prev, self.next = None, None  # Pointers to previous and next Node

# class LRUCache:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.cache = {}  # Hashmap to store key -> pointer to node
#         self.left, self.right = Node(0, 0), Node(0, 0)  # left -> LRU, right -> MRU
#         self.left.next, self.right.prev = self.right, self.left  # Connecting both left and right, will add new node in between of these two
   
#     # Removing node from the list at any position
#     def remove(self, node):
#         prev, nxt = node.prev, node.next
#         prev.next = nxt
#         nxt.prev = prev

#     # Insert node at the rightmost position (making it MRU)
#     def insert(self, node):
#         prev, nxt = self.right.prev, self.right
#         prev.next = nxt.prev = node
#         node.next = nxt
#         node.prev = prev

#     def get(self, key: int) -> int:
#         if key in self.cache:
#             # if key found, remove node from list and insert again at the end
#             self.remove(self.cache[key])
#             self.insert(self.cache[key])
#             return self.cache[key].value
#         return -1

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.remove(self.cache[key])
#         self.cache[key] = Node(key, value)
#         self.insert(self.cache[key])

#         if len(self.cache) > self.capacity:
#             lru = self.left.next  
#             self.remove(lru)
#             del self.cache[lru.key]    

# 3. Usign OrderedDict
class LRUCache:

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)

