def selectionSort(arr):
    n = len(arr)                                
    for i in range(n):                          # Main loop
        min = i                                 # Setting min on first number
        for j in range(i, n):                   # Loop to find new min(smallest number in list)
            if arr[j] < arr[min]:               
                min = j                         
        if i != min:                            # If min will be different than current number(i)
            arr[i], arr[min] = arr[min], arr[i] # Positions of this 2 numbers will be changed
    return arr


array = [7, 5, 3, 6, 1]

print(selectionSort(array))