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

            if item.g < self.table[hash_value][idx].g:
                self.table[hash_value][idx].set_g(item.g)
                self.table[hash_value][idx].set_d(item.d)
                self.table[hash_value][idx].set_prev_n(item.prev_n)
        else:
            self.table[hash_value].append(item)
            self.size += 1

    def is_explored(self, item):
        hash_value = hash(item.state) % self.table_size

        for n in self.table[hash_value]:
            if (n.state == item.state) and (n.g <= item.g):
                return True
        return False
        
    def find(self, item):
        hash_value = hash(item.state) % self.table_size
        if self.table[hash_value] == None:
            return None
        else:
            states = [n.state for n in self.table[hash_value]]
            if item.state in states:
                idx = states.index(item.state)
                return (hash_value, idx)
            
            return None

    def get_by_index(self, hash_value, idx):
        return self.table[hash_value][idx]

