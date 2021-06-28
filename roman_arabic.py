def roman_2_arabic(roman:str)->int:
    roman_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    arabic = 0
    for i in range(0,len(roman)):
        if i+1 not in range(len(roman)):
            arabic += roman_dict.get(roman[i])
        elif roman_dict.get(roman[i]) < roman_dict.get(roman[i+1]):
            arabic -= roman_dict.get(roman[i])
        else:
            arabic += roman_dict.get(roman[i])
    return arabic        
print(roman_2_arabic("MCDL")) 
