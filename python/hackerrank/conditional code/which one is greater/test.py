from task import greater_if_else
from random import randint

tr="The result is: "
i = 0
while i < 100:
    num1 = randint(0,100)
    num2 = randint(0,100)
    if num1>num2:
        ans = tr+str(num1-num2)
    elif num1<num2:
        ans = tr+str(num1+num2)
    else:
        ans = tr+str(num1*num2)
    userans = greater_if_else(num1, num2)
    if ans == userans:
        print("Passed: num1= ".ljust(1)+str(num1).rjust(2)+\
              " num2=".rjust(3)+str(num2).rjust(1)+ \
              " correct ans=".rjust(1)+(ans).strip(tr).rjust(1)+\
              " user ans=".rjust(3)+userans.strip(tr).rjust(4))
    else:break
    i+=1
