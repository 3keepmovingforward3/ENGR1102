from task import primes
import sympy
import filecmp

i=0
primes(100)
input = sympy.ntheory.factor_.factorint(100, multiple=1)
f=open("ans.txt","w")

for i in range(len(input)):
    f.write(str((input[i]))+"\n")
f.close()
print("TestCase=",filecmp.cmp("ans.txt","test.txt"))

i=0
primes(25)
input = sympy.ntheory.factor_.factorint(25, multiple=1)
print(input)
f=open("ans.txt","w")

for i in range(len(input)):
    f.write(str((input[i]))+"\n")
f.close()
print("TestCase=",filecmp.cmp("ans.txt","test.txt"))