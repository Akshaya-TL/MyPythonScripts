def digits(num)->[int]:
    return list(map(int,str(num)))

def factorial(digit)->int:
    facto = 1
    while digit >=1 :
        facto = facto * digit
        digit = digit - 1
    return facto

def is_strong(num)->bool:
    return num == sum(list(map(factorial,digits(num))))

def strong_numbers(limit):
    return [x for x in range(1,limit) if is_strong(x)]


print(strong_numbers(150))

