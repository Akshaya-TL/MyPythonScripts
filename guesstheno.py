import random as r
class game:

    def __init__(self, size):
        self.size = size
        self.secret = self.unique_digits()
        self.cows  = 0
        self.bulls = 0
        self.chances = 0
        
    def unique_digits(self):
        while True:
            self.secret = r.randint(10**(self.size - 1), 10**(self.size) - 1)
            if len(set(str(self.secret))) == self.size:
               return self.secret
    
    def _countbulls_(self, guessed):
         self.bulls = len([x for x in str(guessed) if x in str(self.secret)]) - self.cows
    
    def _countcows_(self, guessed):
         self.cows = len([x for x in zip(str(guessed), str(self.secret)) if x[0] == x[1]])

    def _cows_bulls_check(self, guessed):
        
         self._countcows_(guessed)
         self._countbulls_(guessed)
         self.chances += 1
    
    def finished(self):
        return self.cows == self.size
    
    def result(self):
        return f' cows: {self.cows}  bulls: {self.bulls} \n' 

response = ""
print(" Welcome to the cows and bulls game! ")
x = game(4)
while True:
    guessed = input(" Guess the number: ").upper()
    if guessed not in {"QUIT","Q","REVEAL","EXIT"}:
        x._cows_bulls_check(guessed)
        if not x.finished():
            print(x.result())
        else:
            print(" You have guessed the number right! \n Attempts: ",x.chances)
            break
    else:
        print(" The secret number is ",x.secret)
        break



    
