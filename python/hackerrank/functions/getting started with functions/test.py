import math
from task import factorial

num1=4
num2=6
num3=10
num4=92
numbers = [4,6,10,92]
for i in range(len(numbers)):
    print("\n***Testcase*** =", i)
    print("\ninput: ", numbers[i])
    print("\nexpected output: ", math.factorial(numbers[i]))
    print("\nyour output: ", factorial(numbers[i]))
    if  factorial(numbers[i]) != math.factorial(numbers[i]):
        print("Test Case",i,"Fail")
    else:
        print("Test Case",i,"Passed")
        
    