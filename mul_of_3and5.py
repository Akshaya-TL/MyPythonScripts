def sum_mul(num1,num2):
    return sum([ x for x in range(num1,num2) if x % 3==0 or x % 5 == 0])
print(sum_mul(1,1000))
