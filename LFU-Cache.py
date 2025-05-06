# class LFUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity # Max number of keys in cache
#         self.cache = {}  # Key -> [0 Value, 1 Frequency, 2 Timestamp]
#         self.timestamp = 0 # Counter that gets incremented when item is accessed or inserted
        
#     def get(self, key: int) -> int:
#         if key not in self.cache: # Key not found in cache, return -1
#             return -1

#         # If found, increment the freq, increment the global timestamp and update timestamp of the key to mark it as most recently accessed
#         self.cache[key][1] += 1
#         self.timestamp += 1
#         self.cache[key][2] = self.timestamp

#         return self.cache[key][0]
        
#     def put(self, key: int, value: int) -> None:
#         if self.capacity <= 0: # If capacity is 0 or less than 0
#             return 

#         self.timestamp += 1
#         # If key already present, updating value
#         if key in self.cache:
#             self.cache[key][0] = value  # Updating with new value
#             self.cache[key][1] += 1     # Incrementing the frequency
#             self.cache[key][2] = self.timestamp # Updating timestamp 
#             return  # Returning simply as no eviction is needed

#         # Eviction if cache is full, current length is greater than or equal to capacity
#         if len(self.cache) >= self.capacity:
#             min_freq = float('inf')
#             min_timestamp = float('inf')
#             lfu_key = None

#             # Iterate over all the cache items and find key with min freq or min. timestamp if multiple keys with min freq found
#             for k, (_, freq, ts) in self.cache.items():
#                 if freq < min_freq or (freq == min_freq and ts < min_timestamp):
#                     min_freq = freq
#                     min_timestamp = ts
#                     lfu_key = k
#             if lfu_key is not None:
#                 del self.cache[lfu_key]

#         # Simply adding new key with value
#         self.cache[key] = [value, 1, self.timestamp]
        


# # Your LFUCache object will be instantiated and called as such:
# # obj = LFUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)


class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.left = ListNode(0) # Dummy head
        self.right = ListNode(0, self.left) # Dummy tail
        self.left.next = self.right # Joining head and tail
        self.map = {} # val -> ListNode

    def length(self): # To get the number of keys in current freq bucket
        return len(self.map)

    def pushRight(self, val): # Insert key node at the right end of list making it most recently used
        node = ListNode(val, self.right.prev, self.right)
        self.map[val] = node  # Appending node to the list with key as value
        self.right.prev = node  # Updating prev and next pointers for adding new node at the right
        node.prev.next = node

    def pop(self, val): # Removes node(key) from anywhere in the list in O(1)
        if val in self.map:
            node = self.map[val]
            next, prev = node.next, node.prev
            next.prev = prev
            prev.next = next
            self.map.pop(val, None)

    def popleft(self): # Removes and returns the least recently used key
        res = self.left.next.val
        self.pop(self.left.next.val)
        return res

    def update(self, val):
        self.pop()
        self.pushRight(val)

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfuCnt = 0
        self.valMap = {}
        self.countMap = defaultdict(int)
        self.listMap = defaultdict(LinkedList)


    def counter(self, key):
        cnt = self.countMap[key]
        self.countMap[key] += 1
        self.listMap[cnt].pop(key)
        self.listMap[cnt+1].pushRight(key)

        if cnt == self.lfuCnt and self.listMap[cnt].length() == 0:
            self.lfuCnt += 1

    def get(self, key: int) -> int:
        if key not in self.valMap:
            return -1
        self.counter(key)
        return self.valMap[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return 

        if key not in self.valMap and len(self.valMap) == self.cap:
            res = self.listMap[self.lfuCnt].popleft()
            self.valMap.pop(res)
            self.countMap.pop(res)

        self.valMap[key] = value
        self.counter(key)
        self.lfuCnt = min(self.lfuCnt, self.countMap[key])
    

    
