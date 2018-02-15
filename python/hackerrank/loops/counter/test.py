from task import counter
a = ""
i = 0
n=5
t = 0
while t<9:
    a=""
    print("Input: ",n)
    for i in range(n+1):
        a += str(i)
        a += "\n"
    print("Expected Output:\n"+ a)
    print("\nUser Output: ")
    counter(n)
    f = open("test.txt","r")
    b = f.read()
    if b == a:
        print("Test Case Success")
    else:
        print("Test Case Failed")
        break
    f.close
    n +=1
    t += 1

