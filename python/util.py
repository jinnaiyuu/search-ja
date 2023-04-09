import time

class SearchLogger:
    def __init__(self) -> None:
        self.expanded = 0
        self.generated = 0
        self.pruned = 0

    def start(self):
        self.start_perf_time = time.perf_counter()
        self.start_time = time.time()

    def end(self):
        self.end_perf_time = time.perf_counter()
        self.end_time = time.time()

    def branching_factor(self):
        return self.generated / self.expanded

    def pruned_rate(self):
        return self.pruned / (self.generated + self.expanded)
    
    def time(self):
        return self.end_time - self.start_time
    
    def perf_time(self):
        return self.end_perf_time - self.start_perf_time
    
    def expansion_rate(self):
        return self.expanded / self.time()
    
    def generation_rate(self):
        return self.generated / self.time()
    
    def print(self):
        print("Time: ", self.time())
        print("Perf Time: ", self.perf_time())
        print("Expanded: ", self.expanded)
        print("Generated: ", self.generated)
        print("Pruned: ", self.pruned)
        print("Expansion rate: ", self.expansion_rate())
        print("Generation rate: ", self.generation_rate())
        print("Branching factor: ", self.branching_factor())
        print("Pruned rate: ", self.pruned_rate())
