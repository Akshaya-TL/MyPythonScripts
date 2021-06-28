class fibonacci:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
     
    def next_fibo(self):
        self.next =  self.num1 + self.num2
        return self.next

    def prev_fibo(self):
        self.prev = self.next - self.start
        return self.prev
    
    def fibo_sequence(self,counter):
        self.sequence = [self.num1,self.num2] 
        for i in range(limit-2):
           self.sequence.append(self.num1 + self.num2)
           self.num1 = self.sequence[-1]
           self.num2 = self.sequence[-2]
        return self.sequence

    def access_fibo(self,i):
        return self.sequence[i-1]


myfibo = fibonacci(12,13)
print(myfibo.fibo_sequence(3))
print(myfibo.access_fibo(2))
print(myfibo.next_fibo()) 
print(myfibo.next_fibo()) 
