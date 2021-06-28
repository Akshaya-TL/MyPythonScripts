def letter_count(word1:str)->list:
    
    letter_count_dict = {}
    for i in word1:
        letter_count_dict[i]=word1.count(i)
    return letter_count_dict
print(letter_count("akshaya"))

        


