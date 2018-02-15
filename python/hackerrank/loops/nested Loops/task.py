def primes(num):
    i = 2
    my_list=[]
    f = open("test.txt","w")
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            f.write(str(i)+"\n")
            print(i)
    f.write(str(i)+"\n")
    print(i)
    f.close