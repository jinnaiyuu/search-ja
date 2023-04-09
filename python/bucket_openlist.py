class BucketOpenList:
    def __init__(self, C_min, C_max, beam_width=None):
        self.C_min = C_min
        self.C_max = C_max
        self.bucket = [[] for _ in range(C_max - C_min + 1)]
        self.size = 0
        self.beam_width = beam_width

    def __len__(self):
        return self.size

    def pop(self):
        assert self.size > 0
        for i in range(len(self.bucket)):
            if len(self.bucket[i]) > 0:
                self.size -= 1
                return self.bucket[i].pop()
        assert False

    def push(self, item, priority):
        self.bucket[priority - self.C_min].append(item)
        self.size += 1

        if self.beam_width is not None:
            self.shrink()

    def shrink(self, beam_width=None):
        if beam_width is None:
            beam_width = self.beam_width
        if beam_width is not None:
            cur_C = self.C_max - self.C_min
            while self.size > beam_width:
                if len(self.bucket[cur_C]) > 0:
                    self.bucket[cur_C].pop()
                    self.size -= 1
                else:
                    cur_C -= 1
        