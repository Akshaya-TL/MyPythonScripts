class Odometer():
    DIGITS = "123456789"
    def __init__(self, SIZE):
        if not (1 < SIZE < 9):
            raise ValueError
        self.start = int(Odometer.DIGITS[:SIZE])
        self.limit = int(Odometer.DIGITS[-SIZE:])
        self.current = self.start
        self.size = SIZE

    def __repr__(self):
        return str(self.current)

    def DEBUG(self):
        return '''START: %d LIMIT: %d CURRENT: %d SIZE: %d''' %(self.start, self.limit, self.current, self.size)

    def is_ascending(self):
        s = str(self.current)
        return all(x[0] < x[1] for x in zip(s, s[1:]))

    def next_reading(self, step = 1):
        for _ in range(step):
            if self.current == self.limit:
                self.current = self.start
            else:
                self.current += 1
            while not self.is_ascending():
                self.current += 1
        return self.current 
    
    def distance(self,other):
        if self.size != other.size:
            print("incompatible odometers")
            raise TypeError
        dist = 0
        save = self.current
        while self.current != other.current:
            self.next_reading()
            dist += 1
        self.current = save
        return dist
self = Odometer(4)
self2 = Odometer(4)
self2.current = 1245
print(self.distance(self2))
