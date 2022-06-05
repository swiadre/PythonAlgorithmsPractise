def insertSort(arr):                
    n = len(arr)
    for i in range(1, n):                   # We are starting from second element
        selected = arr[i]                   # Setting pointer for first element
        y = i-1                             # Setting a new varieble
        while y >= 0 and selected < arr[y]: # Starting loop
            arr[y+1] = arr[y]               # Where we are sorting array
            y -= 1 
        arr[y+1] = selected 
    return arr
    
array = [4, 5, 2, 9, 0]

print(insertSort(array))