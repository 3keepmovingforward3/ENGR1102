import pytest
from task import Init_Stage


testCaseInputOne = ('5','15','30')
testCaseInputTwo = ("5","16","57")
testCaseAnswerOne = ("515\n"+"30")
testCaseAnswerTwo = ("516\n"+"57")

one = str(Init_Stage())
assert one == testCaseAnswerOne
if one == testCaseAnswerOne:
    print("Test Case One Pass")
else:
    print("Test Case One Fail")

two = str(Init_Stage())
assert two == testCaseAnswerTwo
if one == testCaseAnswerOne:
    print("Test Case Two Pass")
else:
    print("Test Case Two Fail")
