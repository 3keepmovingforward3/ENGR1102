import sys, difflib
from task import my_sum

print("input\n2\n3\n")
print("Student answer: ", my_sum(2,3))
print("Expected answer: ", 2+3)
if my_sum(2,3) != 5:
    print("incorrect")
    exit(0)
else:
    print("Correct\n")
    
print("input\n12\n1\n")
print("Student answer: ", my_sum(12,1))
print("Expected answer: ", 12+1)
if my_sum(12,1) != 13:
    print("incorrect")
    exit(0)
else:
    print("Correct\n")
    
print("input\n101\n89\n")
print("Student answer: ", my_sum(101,89))
print("Expected answer: ", 101+89)
if my_sum(101,89) != 190:
    print("incorrect")
    exit(0)
else:
    print("Correct\n")