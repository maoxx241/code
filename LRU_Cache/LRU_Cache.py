from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.dic=OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.dic:
            value = self.dic[key]
            del self.dic[key]
            self.dic[key]=value
            return value
        else:
            return -1
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            del self.dic[key]
        elif len(self.dic) >= self.capacity:
            k, v = self.dic.popitem(False)
        self.dic[key]=value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)