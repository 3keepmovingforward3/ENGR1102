from task import getSecondLargest
import numpy

def array():
    i = 0
    while i < 9:
        a = numpy.random.randint(0, 100, size=10)
        if sorted(a)[-2] == getSecondLargest(a):
            print("Test Case",str(i),"Passed","Input",a, "Expected",sorted(a)[-2],"User",getSecondLargest(a))
        else:
            print("No")
        i+=1
array()