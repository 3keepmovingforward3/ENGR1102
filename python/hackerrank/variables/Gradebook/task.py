def grade_avrg():
    
##  
    letters = [80,77,88,95,68]
    summ = float(sum(letters)/len(letters))
    
    if (summ <= 100 and summ > 90) :
        letterGrade = 'A'
    elif (summ <= 90 and summ >= 80) :
        letterGrade = 'B'
    elif (summ < 80 and summ >= 70) :
        letterGrade = 'C'
    elif (summ < 70 and summ >= 60) :
        letterGrade = 'D'
    elif (summ < 60 and summ >= 0) :
        letterGrade = 'F'
    else:
        letterGrade = 'The value compared is not a number equal or between 0 and 100'
    
    return ('Average grade is: ' + str(summ) + ', which is a ' + letterGrade)



