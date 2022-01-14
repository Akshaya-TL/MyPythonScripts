def is_armstrong(n: int) -> bool:
    digits = [int(x) for x in str(n)]
    return n == sum([x ** len(digits) for x in digits])

def make_armstrong(start: int, limit: int) -> [int]:
    return [x for x in range(start, limit) if is_armstrong(x)]

def isArmstrong(n: int) -> bool:
    digits = list(map(int, str(n))) 
    return n == sum(map(lambda r: r ** len(digits), digits))

def makeArmstrong(start: int, limit: int) -> [int]:
    return filter(is_armstrong, range(start, limit))

print(make_armstrong(100, 100000))
print(list(makeArmstrong(100, 100000))


