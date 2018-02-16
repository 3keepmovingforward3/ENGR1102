from task import findSum

i = -440
j = 440
test = True
while (test == True) & (i<500):
    test = (findSum(i,j) == i+j)
    print(i)
    i+=1
    j-=1
    if test == False: break
print("\nTest Cases Passed")