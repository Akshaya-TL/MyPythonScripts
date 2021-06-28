class collatzseq:

    def __init__(self,num):
        self.num = num

    def nxt_collatz(self):
        if self.num % 2 == 0:
            self.num //=  2
            return self.num
        else:
            self.num = self.num * 3 + 1
            return self.num
    
    def collatz_seq(self):
        if self.num == 4:
           return  [4, 2, 1]
        self.save = self.num
        self.num = self.nxt_collatz()
        return [self.save] + self.collatz_seq()

x = collatzseq(10)
print(x.collatz_seq())
