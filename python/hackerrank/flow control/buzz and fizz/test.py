from task import fizzbuzz
import pytest

caseOne = 20
caseTwo = 1
caseThree = 45
caseFour = 9
fizz = "fizz"
buzz = "buzz"
noCase = " This number is not divisible by 3 or 5"

print("Input: ",caseOne)
print("Your Output: ", fizzbuzz(caseOne))
print("Expected Output: ", str(caseOne) + " " + buzz)
assert fizzbuzz(caseOne) == (str(caseOne)+ " "+buzz)
if fizzbuzz(caseOne) == (str(caseOne)+ " "+buzz):
    print("Testcase 1: Success")
else:
    print("Testcase 1: Failed")


print("\nInput: ",caseTwo)
print("Your Output: ", fizzbuzz(caseTwo))
print("Expected Output: ", caseTwo, noCase)
assert fizzbuzz(caseTwo) == (str(caseTwo)+noCase)
if fizzbuzz(caseTwo) == (str(caseTwo)+noCase):
    print("Testcase 2: Success")
else:
    print("Testcase 2: Failed")

    
print("\nInput: ",caseThree)
print("Your Output: ", fizzbuzz(caseThree))
print("Expected Output: ", caseThree, fizz+buzz)
assert fizzbuzz(caseThree) == (str(caseThree)+" "+fizz+buzz)
if fizzbuzz(caseThree) == (str(caseThree)+" "+fizz+buzz):
    print("Testcase 3: Success")
else:
    print("Testcase 3: Failed")


print("\nInput: ",caseFour)
print("Your Output: ", fizzbuzz(caseFour))
print("Expected Output: ", caseFour, fizz)
assert fizzbuzz(caseFour) == (str(caseFour)+" "+fizz)
if fizzbuzz(caseFour) == (str(caseFour)+" "+fizz):
    print("Testcase 4: Success")
else:
    print("Testcase 4: Failed")

