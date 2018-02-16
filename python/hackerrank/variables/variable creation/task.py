import sys
def variables():
    f = open('test.txt', 'w')
    
    #Start your code below (tip: Make sure to indent your code)
    penguin = "Penguin"
    six = "6"
    false = "False"
    none = "None"
    a = "100.66"
    f.write(penguin+"\n")
    f.write(six+"\n")
    f.write(false+"\n")
    f.write(none+"\n")
    f.write(a+"\n")
    
    print(penguin)
    print(6)
    print(false)
    print(none)
    print(a)
    
    f.close()

