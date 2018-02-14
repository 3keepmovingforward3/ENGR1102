from task import in_n_out
import pytest


a = in_n_out()
ansOne = "I Have 20 Total"
if a == ansOne:
    print("Test Case One Passed")
else:
    print("Test Case One Failed")

ansTwo = "I Have 70 Guests!"
b = in_n_out()
if b == ansTwo:
    print("Test Case Two Passed")
else:
    print("Test Case Two Failed")

