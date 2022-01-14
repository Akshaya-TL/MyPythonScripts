def no_duplicate(given : list)->list:
    new_list = []
    for i in given:
        if i not in new_list:
           new_list = new_list + [i]
    return new_list
print(no_duplicate([1,2,2,3,12,3,4,5]))

