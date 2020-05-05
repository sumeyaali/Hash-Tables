
class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity=50):
        self.capacity = capacity
        self.hash_table = [None] * self.capacity
        self.storage = 0


    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        # hash_total= 0
        # #loop through each character in the key
        # for index, c in enumerate(key):
        #     hash_total = (index + len(key)) ** ord(c)
        #     hash_total = hash_total % self.capacity
        # return hash_total
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash
       

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """

        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity



    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        self.buckets = [None] * self.capacity
        """
        self.storage += 1
        index = self.hash_index(key)
        self.hash_table[index] = HashTableEntry(key,value)
        return 



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.hash_table[index]

        while True:
            if node.key == key:
                node.value = None
                return
            elif node.next is None:
                return
            else: 
                node = node.next
            
        

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.hash_table[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else: 
            return node.value

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    # print(ht.get("line_1"))
    # print(ht.get("line_2"))
    # print(ht.get("line_3"))

    # print("")
