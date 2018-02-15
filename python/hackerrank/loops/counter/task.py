def counter(endCount):
    i=0
    f = open("test.txt","w")
    for i in range(endCount+1):
        f.write(str(i)+"\n")
        print(i)
    f.close