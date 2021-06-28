class odometer:
    DIGITS = '123456789'
    def __init__(self,size):
        self.size = size
        self.start = int(odometer.DIGITS[:self.size])
        self.end = int(odometer.DIGITS[-self.size:]
        self.current = self.start

    def is_reading(self):
        return sorted(list(set(str(self.current)))) == list(str(self.current))              
    #all(x[0] < x[1] for x in zip(str(self.num),str(self.num)[1:])

    def next_reading(self, step = 1):
        if self.current == self.end :
           return self.start
        self.current += 1
        while not self.is_reading():
            self.current += 1
        return self.current

    def prev_reading(self,step = 1):
        if self.current == self.start:
           return self.end
        self.current -= 1
        while not self.is_reading(self.current):
             self.current -= 1
        return self.current

    def kth_reading(self, k):
        self.k = k
        self.n = 0
        while self.n != self.k:
            self.current = self.next_reading()
            self.n += 1
        return self.current
    
    def diff(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        self.distance = 0
        while self.num1 !=  self.num2:
            self.num1 = self.next_reading(self.num1)
            self.distance += 1
        return self.distance

    def odometer(self,current):
        self.currentr = current
        return f'{self.start}<<{self.currentr}<<{self.end}'

odo1 = odometer(4)
self.current = 1234
             
   
