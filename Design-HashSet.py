class MyHashSet(object):

    def __init__(self):
        self.data = []

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key not in self.data:
            self.data.append(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.data:
            self.data.remove(key)
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return key in self.data
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)