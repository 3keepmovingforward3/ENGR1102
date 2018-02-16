from task import Wallet

a=(1,5,10,20,50,100)
b=(4,0,5,7,8,12)
c=(100,50,20,10,5,1)
d=(4,8,6,3,4,1)

total = Wallet(a,b)
if total == 1794:
    print("Test Case One Passed")
else:
    print(total)
    print("Expected Ouput: ",1794)


total = Wallet(c,d)
if total == 971:
    print("Test Case Two Passed")
else:
    print(total)
    print("Expected Ouput: ",971)


