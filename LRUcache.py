class DLNode(): 
    def __init__(self):
        self.key = 0
        self.prev = None
        self.next = None
            
class LRU():
    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLNode(), DLNode()

        self.tail.prev = self.head
        self.head.next = self.tail

    def add_node(self, node: DLNode):
        node.prev = self.head
        node.next = self.head.next

        node.next.prev = node
        self.head.next = node

    def remove_node(self, node: DLNode):
        prev = node.prev
        nex = node.next

        prev.next = nex
        nex.prev = prev

    def move_to_head(self, node: DLNode):
        self.remove_node(node)
        self.add_node(node)

    def remove_tail(self):
        res = self.tail.prev
        self.remove_node(res)
        return res


    def get(self, key: str) -> bool:
        node = self.cache.get(key, None)
        if not node:
            return False

        self.move_to_head(node)

        return True

    def put(self, key: str):
        node = self.cache.get(key)

        if not node: 
            newNode = DLNode()
            newNode.key = key

            self.cache[key] = newNode
            self.add_node(newNode)

            self.size += 1

            if self.size > self.capacity:
                tail = self.remove_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            self.move_to_head(node)