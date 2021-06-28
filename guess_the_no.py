import random as r

def secret():
    while True:
        given = r.randint(1000,9999)
        if len(set(str(given))) == 4:
            return given
given = secret()

def cows(guessed, given):
    return len([x for x in zip(guessed, str(given)) if x[0] == x[1]])

def bulls(guessed, given):
    count = 0
    for num in guessed:
        if num in str(given):
            count += 1
    return count - cows(guessed, given)

def guess_the_num():
    count = 1
    guessed = input(' Welcome to the cows and bulls game! \n Enter a number: ')
    chances = 1
    while guessed != str(given):
        print(' cows: ', cows(guessed, given), ' bulls: ', bulls(guessed, given))
        guessed = input(' Enter a number: ')
        chances += 1
    return f' You have guessed it right! \n Chances Taken: %d'%(chances)

print(guess_the_num())
