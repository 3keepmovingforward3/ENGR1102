import pytest
from task import M_G


testCaseInputOne = ('5','16','57')
testCaseInputTwo = ('10','35','27')
testCaseInputThree = ('36','12','24')

testCaseAnswerOne = (78)
testCaseAnswerTwo = (72)
testCaseAnswerThree = (72)

one = M_G()

if one == testCaseAnswerOne:
    print("Test Case One Pass")
else:
    print("Test Case One Fail")

two = M_G()

if two == testCaseAnswerTwo:
    print("Test Case Two Pass")
else:
    print("Test Case Two Fail")
    
three = M_G()

if three == testCaseAnswerThree:
    print("Test Case Three Pass")
else:
    print("Test Case Three Fail")
