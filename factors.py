def factors(num:int):
    fact_list=[num] 
    for i in range(1,(num//2) + 1):
        if num % i == 0:
           fact_list.append(i)
    return sorted((fact_list))
print(factors(5))


def factors2(num:int):
    fact_list = []
    for i in range(1,int(n ** 0.5) + 1):
        div,mod = divmod(n,i)
        if mod == 0:
            result |= {i,div}
print(factors2(121))
