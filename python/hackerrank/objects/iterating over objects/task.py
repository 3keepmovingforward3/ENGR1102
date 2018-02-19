# Complete the function below.

def getCount(objects):
    # Write your code here.
    x=0
    z=len(objects)
    for i in range(z):
        if objects[i].x == objects[i].y:
            x+=1
    return(x)
