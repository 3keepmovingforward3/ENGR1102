from task import variables
import filecmp, os

variables()
a=filecmp.cmp("test.txt","ans.txt")
if a == True:
    print("Test Case Passed")
os.remove("test.txt")