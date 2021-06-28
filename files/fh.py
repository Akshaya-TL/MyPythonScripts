fh = open("names.txt", "w")
names = ["asha", "sweet", "rita"]
for name in range(len(names)):
    print(fh.write(names[name]))
    print("\n") 
fh.close()

