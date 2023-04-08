class HashClosedList:
    def __init__(self, max_size=10000):
        # This assumes that the hash function is not always a perfect hasing.
        self.table = [[]] * max_size
        self.table_size = max_size
        self.size = 0

    def __len__(self):
        return self.size
    
    def push(self, item):
        hash_value = hash(item.state) % self.table_size

        states = [n.state for n in self.table[hash_value]]
        if item.state in states:
            idx = states.index(item.state)
            self.table[hash_value][idx] = item
        else:
            self.table[hash_value].append(item)
            self.size += 1

    def explored(self, item):
        hash_value = hash(item.state) % self.table_size
        if self.table[hash_value] == None:
            return False
        else:
            states = [n.state for n in self.table[hash_value]]
            if item.state in states:
                idx = states.index(item.state)
                node = self.table[hash_value][idx]
                return node.g <= item.g
            
            return False