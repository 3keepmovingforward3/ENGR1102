from task import atm
import os, filecmp

def file_cmp(a,b):
    test = filecmp.cmp(a,b)
    return(test)

def finish_cmp(a,b):
    test = a==b
    return(test)

    
open("finished.txt","w").close() ##clear finished

##open to create
f = open("balance.txt","r")
g = open("finished.txt","r")
h = open("withdraw.txt","r")

##open to create/answer
i = open("withdraw_ans.txt","w")
j = open("main_menu_ans.txt","w")
k = open("deposit_ans.txt","w")
l = open("invalid_ans.txt","w")

i.write("You have selected to withdraw money from the account\n")
i.write("You have $8500.00 left")
i.close()
j.write("Returning to main menu\n")
j.close()
k.write("You have selected to deposit money to the account\n")
k.write("Your new balance is $4000.00")
k.close()
l.write("You have selected an Invalid option\n")
l.close()

##open to compare files
i = open("withdraw_ans.txt","r")
j = open("main_menu_ans.txt","r")


x=atm(9000)
x.withdraw(500)
x.finished("Yes")

test_case_1 = file_cmp("withdraw.txt","withdraw_ans.txt")
m = g.readline()
n = j.readline()
test_case_2 = finish_cmp(m,n)
if test_case_1 == True & test_case_2 == True:
    print("\nTest case 1 passed\n")
else:
    print("\nTest case 1 failed")
j.close()
g.close()


j = open("deposit.txt","r")
g = open("deposit_ans.txt","r")
x=atm(3500)
x.deposit(500)
x.finished("no")
test_case_1 = file_cmp("deposit.txt","deposit_ans.txt")
j.readline()
g.readline()
m = j.readline()
n = g.readline()
test_case_2 = finish_cmp(m,n)
if test_case_1 == True & test_case_2 == True:
    print("\nTest case 2 passed\n")
else:
    print("\nTest case 2 failed")
g.close()
j.close()


x=atm(500)
x.finished("derp")
g = open("finished.txt","r")
g.readline()
g.readline()
j = open("invalid_ans.txt","r")
m = j.readline()
n = g.readline()
test_case_2 = finish_cmp(m,n)
if test_case_1 == True & test_case_2 == True:
    print("\nTest case 2 passed\n")
else:
    print("\nTest case 2 failed")
g.close()
j.close()