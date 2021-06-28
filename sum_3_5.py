def list_num_mul_3_5 (num: int)->[int]:
    mul = []
    for i in range(1,num):
        if i%3==0 or i%5==0:
          mul  += [i]
    return mul

def sum_5_3(num:int)-> int:           
    list1 = list_num_mul_3_5(num)
    t= 0
    for i in list1:
        t += i 
    return t
print(sum_5_3(1000))
