from task import fizzbuzz

caseOne = 20
caseTwo = 1
caseThree = 45
caseFour = 9
fizz = "fizz"
buzz = "buzz"
noCase = " This number is not divisible by 3 or 5"

useranswer=fizzbuzz(caseFour)
testanswer=str(caseFour)+" "+fizz

print("Input: ",caseOne)
print("Your Output: ", fizzbuzz(caseOne))
print("Expected Output: ", str(caseOne) + " " + buzz)
if fizzbuzz(caseOne) == (str(caseOne)+ " "+buzz):
    print("Testcase 1: Success")
else:
    print("Testcase 1: Failed")

print("\nInput: ",caseTwo)
print("Your Output: ", fizzbuzz(caseTwo))
print("Expected Output: ", caseTwo, noCase)
if fizzbuzz(caseTwo) == (str(caseTwo)+noCase):
    print("Testcase 1: Success")
else:
    print("Testcase 1: Failed")
    
print("\nInput: ",caseThree)
print("Your Output: ", fizzbuzz(caseThree))
print("Expected Output: ", caseThree, fizz+buzz)
if fizzbuzz(caseThree) == (str(caseThree)+" "+fizz+buzz):
    print("Testcase 1: Success")
else:
    print("Testcase 1: Failed")

print("\nInput: ",caseFour)
print("Your Output: ", fizzbuzz(caseFour))
print("Expected Output: ", caseFour, fizz)
if fizzbuzz(caseFour) == (str(caseFour)+" "+fizz):
    print("Testcase 1: Success")
else:
    print("Testcase 1: Failed")