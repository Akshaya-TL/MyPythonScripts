def pattern(num):
    for i in range(1,num):
        for j in range(1,i+2):
            if i + j in range(num+1,num+j):

