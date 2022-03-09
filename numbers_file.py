
nmbrs = open("Numbers.txt", "w")
count=0
for i in range(4):
    ddata = input()
    nmbrs.write(str(ddata))
    nmbrs.write("\n")
    count += 1
    if count==4:
        break
nmbrs.close()





