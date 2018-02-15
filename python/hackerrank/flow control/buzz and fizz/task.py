# Complete the function below.

def fizzbuzz(fizzybubbly):
    if (fizzybubbly % 3 == 0) & (fizzybubbly % 5 == 0):
        return(str(fizzybubbly)+" fizzbuzz")
    else:
        if fizzybubbly % 5 == 0:
            return(str(fizzybubbly)+" buzz")
        else:
            if fizzybubbly %3 == 0:
                return(str(fizzybubbly)+" fizz")
            else:
                return(str(fizzybubbly)+ " This number is not divisible by 3 or 5")
        
