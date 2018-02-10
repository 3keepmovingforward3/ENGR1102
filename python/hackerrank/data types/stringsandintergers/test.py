import sys, difflib
from task import count_eggs

johnandmaryhave = "John and Mary have "
eggstotal = " eggs total!"

print("input\n6\n7\n")
print("Student answer: ", count_eggs(6,7))
print("Expected answer: ", johnandmaryhave + "13" + eggstotal)
if count_eggs(6,7) != (johnandmaryhave + "13" + eggstotal):
    print("incorrect")
    exit(0)
else:
    print("Correct\n")
    
print("input\n17\n28\n")
print("Student answer: ", count_eggs(17,28))
print("Expected answer: ", johnandmaryhave + "45" + eggstotal)
if count_eggs(17,28) != (johnandmaryhave + "45" + eggstotal):
    print("incorrect")
    exit(0)
else:
    print("Correct\n")
    
print("input\n42\n99\n")
print("Student answer: ", count_eggs(42,99))
print("Expected answer: ", johnandmaryhave + "141" + eggstotal)
if count_eggs(42,99) != (johnandmaryhave + "141" + eggstotal):
    print("incorrect")
    exit(0)
else:
    print("Correct\n")