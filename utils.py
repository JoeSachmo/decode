from sets import Set

class MySet:
    def __init__(self, theSet):
        self.coverage = theSet
    
    def __hash__(self):
        y = sorted(self.coverage)
        return hash(tuple(y))
    
    def __eq__(self, other):
        return self.coverage == other.coverage
    
    def add(self, element):
        self.coverage.add(element)
    
    def copy(self):
        return self.coverage.copy()
    
    def __str__(self):
        return self.coverage.__str__()
    
class QueueKey:
    def __init__(self, lm_state, coverage, heuristic):
        self.lm_state = lm_state
        self.coverage = coverage
        self.heuristic = heuristic
        
    def __hash__(self):
        y = sorted(self.coverage.copy())
        return hash((self.lm_state, tuple(y)))
    
    def __eq__(self, other):
        return (self.lm_state, self.coverage) == (other.lm_state, other.coverage)


