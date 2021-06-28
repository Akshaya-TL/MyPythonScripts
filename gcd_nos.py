def gcd_of_nos(num1:int,num2:int)->int:
    if num2 == 0:
        return num1
    return gcd_of_nos(num2,num1%num2) 

def lcm_of_nos(num1:int,num2:int)->int:
    return (num1*num2)//gcd_of_nos(num1,num2)

def gcd_lcm(num1:int,num2:int)->[int]:
    return gcd_of_nos(num1,num2) , lcm_of_nos(num1,num2)
    

print(gcd_lcm(50,10))
