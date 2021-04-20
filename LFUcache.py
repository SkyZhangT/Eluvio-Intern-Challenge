import collections

class DLNode:
    def __init__(self, key):
        self.key = key
        self.freq = 1
        self.prev = self.next = None

class DLList:
    def __init__(self):
        self._trav = DLNode(None)
        self._trav.next = self._trav.prev = self._trav
        self.size = 0
    
    def append(self, node: DLNode):
        node.next = self._trav.next
        node.prev = self._trav
        node.next.prev = node
        self._trav.next = node
        self.size += 1
    
    def pop(self, node: DLNode = None):
        if self.size == 0:
            return
        
        if not node:
            node = self._trav.prev

        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        
        return node
        
class LFU:
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        
        self.cache = dict()
        self.freq_map = collections.defaultdict(DLList)
        self.min_freq = 0
        
    def update(self, node: DLNode):
        freq = node.freq
        
        self.freq_map[freq].pop(node)
        if self.min_freq == freq and not self.freq_map[freq]:
            self.min_freq += 1
        
        node.freq += 1
        freq = node.freq
        self.freq_map[freq].append(node)
    
    def get(self, key: str) -> bool:
        if key not in self.cache:
            return False
        
        node = self.cache[key]
        self.update(node)
        return True

    def put(self, key: str):
        if self.capacity == 0:
            return
        
        if key in self.cache:
            node = self.cache[key]
            self.update(node)
        else:
            if self.size == self.capacity:
                node = self.freq_map[self.min_freq].pop()
                del self.cache[node.key]
                self.size -= 1
                
            node = DLNode(key)
            self.cache[key] = node
            self.freq_map[1].append(node)
            self.min_freq = 1
            self.size += 1