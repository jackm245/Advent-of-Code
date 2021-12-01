class Node(object):
    def __init__(self, parent, value, prev, next_):
        assert isinstance(parent, LinkedList)
        self.parent = parent
        self.value = value
        self.prev = prev
        self.next = next_
    def insert(self, x):
        node = Node(self.parent, x, self, self.next)
        self.parent.D[x] = node
        self.next = node
        node.next.prev = node
        return node
    def erase(self):
        self.next.prev = self.prev
        self.prev.next = self.next
        del self.parent.D[self.value]

class LinkedList(object):
    def __init__(self):
        self.D = {}
    def append(self, prev, x):
        if prev is None:
            node = Node(self, x, None, None)
            node.next = node
            node.prev = node
            self.D[x] = node
            return node
        else:
            node = Node(self, x, prev, prev.next)
            prev.next = node
            node.next.prev = node
            self.D[x] = node
            return node

    def find(self, x):
        return self.D[x]

    def to_list(self, start):
        node = self.D[start]
        ret = [node.value]
        node = node.next
        while node.value != start:
            ret.append(node.value)
            node = node.next
        return ret
