def min(arr):
    min = arr[0]                 # Setting first element as a min
    for i in range(1, len(arr)): # Loop that check every element in array excluding first because it is already min
        if arr[i] < min:         # If current element is smaller than min 
            min = arr[i]         # Set this element to min

    return min


array = [9, 3, 5, 2, 1, 5, 0, 2]
print(min(array))