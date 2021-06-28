def factorial(num:int):
    n = num
    fact = 1 
    for n in range(1,num+1):
       fact *= n
       n = n-1 
    return fact
print(factorial(4))

    
