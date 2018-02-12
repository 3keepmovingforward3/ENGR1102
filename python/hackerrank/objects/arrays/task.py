# Complete the function below.

def getSecondLargest(nums):
    # Write your code here.
    i = nums[0];
    for i in range(0,i-1):
        j = nums[i]
        if nums[i+1] > j:
            j = nums[i+1]
        
        