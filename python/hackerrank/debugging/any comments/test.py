from task import findLargestNum
import numpy
i = 0
while i < 10:
    test=numpy.random.randint(2,100, size=10)
    if max(test) == findLargestNum(test):
        print("yes")
    i+=1
