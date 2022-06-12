def max(arr):
    max = arr[0]                 # Setting first element as a max
    for i in range(1, len(arr)): # Loop that check every element in array excluding first because it is already max
        if arr[i] > max:         # If current element is bigger than max 
            max = arr[i]         # Set this element to max

    return max


array = [9, 3, 5, 2, 1, 5, 0, 2]
print(max(array))