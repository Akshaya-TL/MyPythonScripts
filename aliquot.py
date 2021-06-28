#list of aliquot numbers by recursion method

def factors(num : int) -> [int]:
    fact_list = []
    for i in range(1,int(num**0.5)+1):
        quo,rem = divmod(num,i)
        if  rem == 0:
           fact_list += [i,quo]
    return sorted(fact_list)

def aliquot(num : int) -> [int]:
    next_num = sum(factors(num)) - num
    if next_num == 1:
        return  [1]
    return [num] + aliquot(next_num)
print(aliquot(4))
