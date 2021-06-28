class fibonacci:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        self.save1 = num1
        self.save2 = num2
     
    def next_fibo(self):
        self.next = self.save1 + self.save2
        self.save1, self.save2 = self.save2, self.next
        return self.next
    

    def prev_fibo(self):
        self.prev = self.save2 - self.save1
        self.save2, self.save1 = self.save1,self.prev
        return self.prev
    
    def fibo_sequence(self,count):
        self.sequence = [self.num1,self.num2] 
        for i in range(count-2):
           self.sequence.append(self.next_fibo())
        return self.sequence

    def access_fibo(self,i):
        k = 0
        if i == 1:
            return self.num1
        if i == 2:
            return self.num2
        while k != i-2:
           self.element = self.next_fibo()
           k += 1
        return self.element

