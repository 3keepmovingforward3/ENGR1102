def counter(endCount):
    f = open("test.txt","w")
    ###User Code Below###
    
    i=0
    for i in range(endCount+1):
        f.write(str(i)+"\n")
        print(i)
    
    ###End User Code###
    f.close