def is_reading(num : int)->bool:
    ls = []
    for i in str(num):
         ls.append(str(num).count(i))
    if len(set(ls)) == 1:
         return sorted(str(num)) == str(num)
    else:
        return False
print(is_reading(1987))
#def odometer_readings(size : int):
#    return [num for num in range(10**(size-1),10**(size)) if is_reading(num)]
#print(odometer_readings(3))
