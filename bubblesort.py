def bubblesort(arr):
    n = len(arr)                                    # Optimalizating code we can check the array lenght just once
    for i in range(n-1):                            # Makeing a first loop
        for j in range(0, n-i-1):                   # And second to check every single option to sort
            if arr[j+1] < arr[j]:                   # If first first element is greater than second
                arr[j+1], arr[j] = arr[j], arr[j+1] # Swap it
    return arr

array = [2,4,3,6,1]

print(bubblesort(array))