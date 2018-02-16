# This is a comment. Text formatted with /.../ is ignored when the code runs.
 # The next line of code that the computer will evaluate starts with the word "function"
 # A function is a user-defined command that you'll learn how to create in the future
 # The HackerRank system uses functions as its basic building block to give you feedback.
 # For now, you're just filling in the details.
 # Type your code where instructed below.

def greater_if_else(num1, num2):
    tr="The result is: "
    #Start your code below (tip: Make sure to indent your code)
    if num1>num2:
        return(tr+str(num1-num2))
    elif num1<num2:
        return(tr+str(num1+num2))
    else:
        return(tr+str(num1*num2))

