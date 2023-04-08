class BucketOpenList:
    def __init__(self, C_min, C_max):
        self.C_min = C_min
        self.C_max = C_max
        self.bucket = [[] for _ in range(C_max - C_min + 1)]
        self.size = 0

    def __len__(self):
        return self.size

    def pop(self):
        assert self.size > 0
        for i in range(len(self.bucket)):
            if len(self.bucket[i]) > 0:
                self.size -= 1
                return self.bucket[i].pop(0)
        assert False

    def push(self, item, priority):
        self.bucket[priority - self.C_min].append(item)
        self.size += 1