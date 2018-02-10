import sys, difflib
from task import my_print

stranswer = " I Love ENGR 1102!"
str1 = "Hello, World!"
str2 = "Do you know de way?"
str3 = "She's da queen!"
#orig_stdout = sys.stdout
#f = open('out.txt', 'w')
#sys.stdout = f
print("Input:\n" + str1)
print("\nYour Output:\n" + my_print(str1))
print("Expected Output:\n" + str1 + stranswer)
testcase1 = (str1 + stranswer)
if testcase1 != my_print(str1):
    print("Test Case Failed")
else:
    print("Test Case Success")

print("Input:\n" + str2)
print("\nYour Output:\n" + my_print(str2))
print("Expected Output:\n" + str2 + stranswer)
testcase1 = (str2 + stranswer)
if testcase1 != my_print(str2):
    print("Test Case Failed")
else:
    print("Test Case Success")
    
print("Input:\n" + str3)
print("\nYour Output:\n" + my_print(str3))
print("Expected Output:\n" + str3 + stranswer)
testcase1 = (str3 + stranswer)
if testcase1 != my_print(str3):
    print("Test Case Failed")
else:
    print("Test Case Success")



#sys.stdout = orig_stdout
#f.close()

#file = open('out.txt', 'r')
#answer = file.read()
#print(answer)
#diff = difflib.ndiff(answer.strip(), correctAnswer)
#print(''.join(diff))