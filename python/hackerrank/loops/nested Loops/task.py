def primes(num):
    f = open("test.txt","w")
    
    ##Enter User Code Below###

    i = ____
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            f.write(str(i)+"\n")
            print(i)
    print(i)
    
    
    ###End User Code
    f.write(str(i)+"\n")
    f.close