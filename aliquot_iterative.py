def factors(num : int)->[int]:
    return [i for i in range(1,int(num*0.5)+1) if num % i == 0]


def aliquot(num : int)->[int]:

    if num == sum(factors(num)):
        return [num],'perfect number'
    elif sum(factors(sum(factors(num)))) == num:
        return [num,sum(factors(num))],'amicable pairs'
    elif num ==1:
        return [1]
    return [num] + aliquot(sum(factors(num)))


print(aliquot(220))
print(aliquot(6))
print(aliquot(10))
