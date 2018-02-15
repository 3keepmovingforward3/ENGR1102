import math
from task import nth_fact

i = 0
while i<7:
    if nth_fact(i)==math.factorial(i):
        print("Test Case Input",i,"Pass")
    else:
        break
    i+=1