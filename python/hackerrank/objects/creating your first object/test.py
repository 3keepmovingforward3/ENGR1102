from task import Rectangle

try_zero = Rectangle(4,5)
try_one = Rectangle(14,20)
try_two = Rectangle(20,20)
ansTryZero = [4,5,18,20]
ansTryOne = [14,20,68,280]
ansTryTwo = [20,20,80,400]

#and try_zero.getPerimeter() != ansTryZero[2] and try_zero.length != ansTryZero[0] and try_zero.width != ansTryZero[1]

print("Input: \n4\n5\n")
print("Expected output: 4 5 18 20")
print("User output:    ",try_zero.length, try_zero.width,try_zero.getPerimeter(),try_zero.getArea())
if (try_zero.getArea() == ansTryZero[3]) & (try_zero.getPerimeter() == ansTryZero[2]) & (try_zero.width == ansTryZero[1]) & (try_zero.length == ansTryZero[0]):
    print("Testcase Passed!!!")
else:
    print("Testcase Failed!!!\n")

print("Input: \n14\n20\n")
print("Expected output: 14 20 68 280")
print("User output:    ",try_one.length, try_one.width,try_one.getPerimeter(),try_one.getArea())
if (try_one.getArea() == ansTryOne[3]) & (try_one.getPerimeter() == ansTryOne[2]) & (try_one.width == ansTryOne[1]) & (try_one.length == ansTryOne[0]):
    print("Testcase Passed!!!")
else:
    print("Testcase Failed!!!\n")


print("Input: \n20\n20\n")
print("Expected output: 20 20 80 400")
print("User output:    ",try_two.length, try_two.width,try_two.getPerimeter(),try_two.getArea())
if (try_two.getArea() == ansTryTwo[3]) & (try_two.getPerimeter() == ansTryTwo[2]) & (try_two.width == ansTryTwo[1]) & (try_two.length == ansTryTwo[0]):
    print("Testcase Passed!!!")
else:
    print("Testcase Failed!!!\n")
    
