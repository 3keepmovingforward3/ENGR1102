def modifyArray(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] = arr[i] * 2
        else:
            arr[i] = arr[i] * 3
    return arr