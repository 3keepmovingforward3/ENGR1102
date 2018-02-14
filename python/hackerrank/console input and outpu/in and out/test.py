from task import in_n_out
import difflib

print("Expected Input: \n5\nI Have\n15\nTotal")
a = in_n_out()
ansOne = "I Have 20 Total"
print("\nExpected Output:", ansOne)
print("User Ouput: ", a)

if a == ansOne:
    print("Test Case One Passed\n")
else:
    diff = difflib.ndiff(a,ansOne)
    print(''.join(diff))
    print("Test Case One Failed\n")
    exit(0)
    
ansTwo = "Welcome to 70 Guests!"
print("Expected Input: \n55\nWelcome to\n15\nGuests!")
b = in_n_out()
print("User Ouput: ", b)
if b == ansTwo:
    print("Test Case Two Passed")
else:
    diff = difflib.ndiff(b,ansTwo)
    print(''.join(diff))
    print("Test Case Two Failed")

