DIGITS = '123456789'

def is_reading(n: int) -> bool:
    s = str(n)
    return all([x[0] < x[1] for x in zip(s,s[1:])])

def FIRST_READING(size: int) -> int:
    return int(DIGITS[:size])

def LAST_READING(size: int) -> int:
    return int(DIGITS[-size:])

def NEXT_READING(n: int) -> int:
    if n == LAST_READING(len(str(n))):
        n =  FIRST_READING(len(str(n)))
    else:
       n += 1
       while not is_reading(n):
          n += 1
    return n

def PREV_READING(n: int) -> int:
    if n == FIRST_READING:
       return LAST_READING
    n -= 1
    while not is_reading(n):
        n -= 1
    return n

def kth_reading(n,k: int) -> int:
    distance = 0
    while  distance != k:
           n = NEXT_READING(n)
    return n

def diff(n,p: int) -> int:
    distance = 0
    while n != p:
        n = NEXT_READING(n)
        distance += 1
    return distance

def odometer(size: int) -> [int]:
    return [x for x in range(10**(size)) if is_reading(x)]

print(diff(6789,1234))
print(kth_reading(1234,10))
print(PREV_READING(1234))
print(NEXT_READING(1245))
print(odometer(3))
          


