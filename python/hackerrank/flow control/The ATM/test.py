from task import withdraw, deposit, cancel, default
import filecmp, difflib, os



##WITHDRAW##
withdraw()
f = open("test.txt","r")
ans = open("ans.txt","w")
ans.write("You have selected to withdraw money from the account.")
ans.close()
ans = open("ans.txt","r")

if filecmp.cmp("test.txt","ans.txt") == True:
    print("Test Case Withdraw Passed\n")
else:
    diff = difflib.ndiff(f.readline(),ans.readline())
    print(''.join(diff), end="")
    print("\n")
f.close()
ans.close()


##DEPOSIT TEST CASE##

deposit()
f = open("test.txt","r")
ans = open("ans.txt","w")
ans.write("You have selected to deposit money to the account.")
ans.close()
ans = open("ans.txt","r")

if filecmp.cmp("test.txt","ans.txt") == True:
    print("Test Case Deposit Passed\n")
else:
    diff = difflib.ndiff(f.readline(),ans.readline())
    print(''.join(diff), end="")
    print("\n")
f.close()
ans.close()

##CANCEL TEST CASE##
cancel()
f = open("test.txt","r")
ans = open("ans.txt","w")
ans.write("Returning to account selection.")
ans.close()
ans = open("ans.txt","r")

if filecmp.cmp("test.txt","ans.txt") == True:
    print("Test Case Cancel Passed\n")
else:
    diff = difflib.ndiff(f.readline(),ans.readline())
    print(''.join(diff), end="")
    print("\n")
f.close()
ans.close()

##DEFAULT TEST CASE##
default()
f = open("test.txt","r")
ans = open("ans.txt","w")
ans.write("You have selected an invalid option.")
ans.close()
ans = open("ans.txt","r")

if filecmp.cmp("test.txt","ans.txt") == True:
    print("Test Case Invalid Passed\n")
else:
    diff = difflib.ndiff(f.readline(),ans.readline())
    print(''.join(diff), end="")
    print("\n")
f.close()
ans.close()
os.remove("test.txt")
os.remove("ans.txt")

