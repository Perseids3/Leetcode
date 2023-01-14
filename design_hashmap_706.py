class ListNode:
    def __init__(self, key, val):
        self.val = [key, val]
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tablesize = 1003;
        self.table = [None]*self.tablesize
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        index = key % self.tablesize
        if self.table[index] == None:
            self.table[index] = ListNode(key, value)
        else:
            cur = self.table[index]
            while True:
                if cur.val[0] == key:
                    cur.val= [key, value] #update
                    return
                if cur.next == None: break
                cur = cur.next
            cur.next = ListNode(key, value)
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key % self.tablesize
        cur = self.table[index]
        while cur:
            if cur.val[0] == key:
                return cur.val[1]
            else:
                cur = cur.next
        return -1
            
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        index = key % self.tablesize
        cur = prev = self.table[index]
        if not cur: return
        if cur.val[0] == key:
            self.table[index] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.val[0] == key:
                    prev.next = cur.next
                    break
                else:
                    cur, prev = cur.next, prev.next
                


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)