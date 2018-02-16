# Complete the function below.

def actuator(pressureWanted, pressureReading, decision):
    # Write your code here.
    for i in range(len(pressureWanted)):
        if pressureWanted[i] < 0 or pressureWanted[i] > 5:
            pressureWanted[i] = 0
    for i in range(len(pressureWanted)):
        if pressureReading[i] < pressureWanted[i]:
            decision[i] = 0
        elif pressureReading[i] > pressureWanted[i]:
            decision[i] = 1
        else:
            decision[i] = 2
    return(decision)
