"""
Design a Hash Table class.

Your HashTable class should support the following operations:

HashTable(int capacity) will initialize an empty hash table with a capacity of capacity, where capacity > 1.
int get(int key) will return the value associated with the key. If the key is not present in the hash table, return -1.
void insert(int key, int value) will insert the key-value pair into the hash table. If the key is already present in the hash table, the original value should be replaced with the new value.
bool remove(int key) will remove the key-value pair with the given key. If the key is not present, return false, otherwise return true
int getSize() will return the number of keys in the hash table.
int getCapacity() will return the capacity of the hash table.
void resize() will double the capacity of the hash table. This method should be called automatically when the load factor reaches or exceeds 0.5. Your insert method should automatically call resize() when necessary.
Note: You can choose how to handle collisions.

"""

class Hashtable():
    def __init__(self,cap):
        self.cap = cap
        self.table = [None] * cap
        self.loadfactor = 0.5
        self.size = 0

    def get(self,key):
        index = self.hashandbucket(key)
        if self.table[index]:
            return self.table[index]
        else:
            return -1


    def insert(self,key, val):
        
        ratio = self.size/self.cap

        if ratio >= 0.5:
            print(ratio)
            self.resize()

        index = self.hashandbucket(key)
        print("ins - ",index)
        self.table[index]=val
        self.size += 1
        

    def remove(self,key) -> bool:
        index = self.hashandbucket(key)
        print(index)
        if self.table[index]:
            self.table[index] = None
            self.size -=1
            return True
        else:
            return False

    def getSize(self):
        return self.size

    def getCapacity(self):
        return self.cap

    def resize(self):
        self.cap = 2 * self.cap
        newtable = [None] * self.cap
        for i, val in enumerate(self.table):
            newtable[i] = val
        self.table = newtable

    def hashandbucket(self,key):
        hashval = hash(key)
        bucketindex = hashval % self.cap
        return bucketindex




ht = Hashtable(5)
print(ht.getSize())
print(ht.getCapacity())
ht.insert(2, 2)
ht.insert(3, 3)
ht.insert(4, 4)
ht.insert(5, 5)
ht.insert(6, 6)
ht.insert(7, 7)
print(ht.table)
print(ht.get(2))
print(ht.get(4))
print(ht.getSize())
print(ht.getCapacity())
ht.remove(2)
print(ht.table)