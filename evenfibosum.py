class fibonacci:
    def __init__(self, limit):
        self.limit = limit
        self.a, self.b = 0, 1
        self.fiboseq = [0]

    def fibo_seq(self):
        while self.b <= self.limit:
            self.fiboseq.append(self.b)
            self.a, self.b = self.b, self.a + self.b
        return self.fiboseq

    def even_fibo_sum(self):
        return sum(filter(lambda x: x % 2 == 0, self.fibo_seq()))

x = fibonacci(4000000)
print(x.even_fibo_sum())
