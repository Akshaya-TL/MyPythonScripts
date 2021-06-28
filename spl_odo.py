# 2 digit odometer
def odo_2()->[int]:
    return [x*10 + y for x in range(1,9) for y in range(2,10) if x<y]

# 4 digit odometer 
def odo_4()->[int]:
    return [w*1000 + x*100 + y*10 + z for w in range(1,10) for x in range(1,10) for y in range(1,10) for z in range(1,10) if w<x<y<z]


print(odo_2())
print(odo_4())
print(odo_2() + odo_4())
