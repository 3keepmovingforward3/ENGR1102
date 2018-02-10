from task import modifyArray


tryOne = [5,1,2,3,4,5]
tryTwo = [8,1,3,4,5,8,11,14,19]
tryThree = [10,33,31,27,25,22,21,18,14,13,12]
ansOne = [0]*len(tryOne)
ansTwo =[0]*len(tryTwo)
ansThree = [0]*len(tryThree)


for i in range(len(tryOne)):
    if tryOne[i] % 2 == 0:
        ansOne[i] = tryOne[i] * 2
    else:
        ansOne[i] = tryOne[i] * 3
        
for i in range(len(tryTwo)):
    if tryTwo[i] % 2 == 0:
        ansTwo[i] = tryTwo[i] * 2
    else:
        ansTwo[i] = tryTwo[i] * 3
        
for i in range(len(tryThree)):
    if tryThree[i] % 2 == 0:
        ansThree[i] = tryThree[i] * 2
    else:
        ansThree[i] = tryThree[i] * 3

userAnswerOne = modifyArray(tryOne)
userAnswerTwo = modifyArray(tryTwo)
userAnswerThree = modifyArray(tryThree)

if userAnswerOne == ansOne:
    print("Input: ", tryOne)
    print("User output: ", userAnswerOne)
    print("Expect output: ", ansOne)
    print("Test Case One Passed\n")
else:
    print("Input: ", tryOne)
    print("User output: ", userAnswerOne)
    print("Expect output: ", ansOne)
    print("Test Case One Failed")
    
if userAnswerTwo == ansTwo:
    print("Input: ", tryTwo)
    print("User output: ", userAnswerTwo)
    print("Expect output: ", ansTwo)
    print("Test Case Two Passed\n")
else:
    print("Input: ", tryTwo)
    print("User output: ", userAnswerTwo)
    print("Expect output: ", ansTwo)
    print("Test Case Two Passed")
    
if userAnswerThree == ansThree:
    print("Input: ", tryThree)
    print("User output: ", userAnswerThree)
    print("Expect output: ", ansThree)
    print("Test Case Three Passed")
else:
    print("Input: ", tryTwo)
    print("User output: ", userAnswerTwo)
    print("Expect output: ", ansTwo)
    print("Test Case Three Failed")

        