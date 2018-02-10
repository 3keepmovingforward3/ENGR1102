from task import Rectangle

try_zero = Rectangle(6,8)
try_one = Rectangle(12,7)
try_two = Rectangle(5,9)
try_three = Rectangle(10,10)
ansTryZero = [48,28]
ansTryOne = [84,38]
ansTryTwo = [45,28]
ansTryThree = [100,40]

print("Input: \n6\n8\n")
print("Expected output: 48 28")
print("User output:    ",try_zero.getArea(),try_zero.getPerimeter())
if try_zero.getArea() != ansTryZero[0] and try_zero.getPerimeter() != ansTryZero[1]:
    print("Testcase Failed!!!")
else:
    print("Testcase Passed!!!\n")

print("Input: \n12\n7\n")
print("Expected output: 84 38")
print("User output:    ",try_one.getArea(),try_one.getPerimeter())
if try_one.getArea() != ansTryOne[0] and try_one.getPerimeter() != ansTryOne[1]:
    print("Testcase Failed!!!")
else:
    print("Testcase Passed!!!\n")

print("Input: \n5\n9\n")
print("Expected output: 45 28")
print("User output:    ",try_two.getArea(),try_two.getPerimeter())
if try_two.getArea() != ansTryTwo[0] and try_two.getPerimeter() != ansTryTwo[1]:
    print("Testcase Failed!!!")
else:
    print("Testcase Passed!!!\n")
    

    
print("Input: \n10\n10\n")
print("Expected output: 100 40")
print("User output:    ",try_three.getArea(),try_three.getPerimeter())
if try_three.getArea() != ansTryThree[0] and try_three.getPerimeter() != ansTryThree[1]:
    print("Testcase Failed!!!")
else:
    print("Testcase Passed!!!\n")

