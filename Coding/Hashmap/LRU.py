from collections import deque
class LRUCache():
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.deq = deque()

    def put(self, key, value):
        if len(self.cache) == self.capacity:
            evictkey = self.deq.popleft()
            self.cache.remove(evictkey)
        self.cache[key] = value
        self.deq.append(key)

    def get(self, key):
        value = self.cache.get(key, None)
        if value:
            self.movetoend(key)
        return value

    def movetoend(self, key):
        self.deq.remove(key)
        self.deq.append(key)


cache = LRUCache(4)


cache.put(1, 1)
cache.put(2, 2)

print(cache.deq)

print(cache.get(1))

print(cache.deq)

cache.put(3, 3)
cache.put(4, 4)
print(cache.get(3))
print(cache.deq)


def decode(s):
    if '[' not in s:
        return s
    i = j = 0
    num = ""
    stack = []
     out = []
      while j < len(s):
           if s[j] == '[':
                num = s[i:j]
                i = j+1
                stack.append('[')
            if s[j] == ']':
                stack.pop()
                if not stack:
                    out.append(int(num) * decode(s[i:j]))
                    i = j+1
            j += 1
    return "".join()
