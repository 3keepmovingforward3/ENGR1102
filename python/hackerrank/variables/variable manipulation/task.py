# This is a comment. Text formatted with /.../ is ignored when the code runs.
 # The next line of code that the computer will evaluate starts with the word "function"
 # A function is a user-defined command that you'll learn how to create in the future
 # The HackerRank system uses functions as its basic building block to give you feedback.
 # For now, you're just filling in the details.
 # Type your code where instructed below.

def var_manipulation():
    #Start your code below (tip: Make sure to indent your code)
    var0 = 3.27
    var1 = 18
    var2 = True
    var3 = 7
    
    ## Do not change the conditional statements below

    if (var0 == 3.27) or (var1 == 5):
        if (var2 == True) & (var3 == 7):
            result = var0 * var3
            return("Here is the result! " + str(result))
        else :
            return("error in second if statement")
    else :
        return("error in first if statement")
    
print(var_manipulation())