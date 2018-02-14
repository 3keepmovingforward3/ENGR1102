from task import M_G


testCaseInputOne = ("5 "+"16 "+"57")
testCaseInputTwo = ('10','35','27')
testCaseInputThree = ('36','12','24')

testCaseAnswerOne = (78)
testCaseAnswerTwo = (72)
testCaseAnswerThree = (72)
print("Input Expected:", testCaseInputOne)
one = M_G()
print("User output", one)
print("Expected ouput",testCaseAnswerOne)
if one == testCaseAnswerOne:
    print("Test Case One Pass")
else:
    print("Test Case One Fail")

print("Input Expected:", testCaseInputTwo)
two = M_G()
print("User output", two)
print("Expected ouput",testCaseAnswerTwo)

if two == testCaseAnswerTwo:
    print("Test Case Two Pass")
else:
    print("Test Case Two Fail")

print("Input Expected:", testCaseInputTwo)
three = M_G()
print("User output", three)
print("Expected ouput",testCaseAnswerThree)

if three == testCaseAnswerThree:
    print("Test Case Three Pass")
else:
    print("Test Case Three Fail")
