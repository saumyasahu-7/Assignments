from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.occupied=0
        self.priority=deque()
        self.cache={}

    def give_first_priority_if_present_already(self, key):
        self.priority.remove(key)
        self.priority.appendleft(key)

    def give_first_priority_if_not_present_already(self, key):
        self.priority.appendleft(key)

    def remove_lru(self):
        del self.cache[self.priority.pop()]
        
    def get(self, key:int)-> int:
        if(key in self.cache.keys()):
            value=self.cache[key]
            self.give_first_priority_if_present_already(key)
            return value
        else:
            return -1

    def put(self, key: int, value: int):
        if(key in self.cache.keys()):
            self.cache[key]=value
            self.give_first_priority_if_present_already(key)
        else:
            self.cache[key]=value
            if(self.occupied<self.capacity):
                self.give_first_priority_if_not_present_already(key)
                self.occupied+=1
            else:
                self.remove_lru()
                self.give_first_priority_if_not_present_already(key)


