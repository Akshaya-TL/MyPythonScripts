'''import fibonacciclass as fib
f = fib.fibonacci(0, 1)
fh = open("fib_file.txt", "w")
'''

        





















fh = open(MYFILE.txt, "w")
mystr1 = "This is my string 1"
mystr2 = "This is my string 2"

fh.write(mystr1)
fh.write("\n")
fh.write(mystr2)
fh.close()

l1 = ["1", "2", "3", "4", "5"]
fo = open("NUMBERS.txt", "w")
fo.writelines(l1)
fo.close()
'''
'''l1 = [1, 2, 3, 4, 5]
fo = open("NUMBERS.txt", "w")

nstr= list(map(lambda x: x + " ", map(str, l1)))
#fo.writelines(nstr)
fo.write(" ".join(nstr))
fo.close()

with open("NUMBERS.txt") as fh:
    print(fh.read(3))
    print(fh.read())'''
'''fo =  open("_1to20.txt", "w")
nstr = list(map(lambda x: x + " ",map(str, [i for i in range(1,21)])))
fo.writelines(nstr)
fo.close()
with open("_1to20.txt") as fh:
    for i in range(4):
        if i < 2:
           print(fh.readline(10))
        else:
           print(fh.readline(15)) '''
