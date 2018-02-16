# Complete the function below.
##ARRAYS IS BROKEN

def getSecondLargest(nums):
    # Write your code here.
    i = len(nums);
    for i in range(0,i-1):
        j = nums[i]
        if nums[i+1] > j:
            j = nums[i+1]
    return(j)    
        