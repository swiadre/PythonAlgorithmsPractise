def isEmpty(arr):
    if(len(arr) > 0): # Simple check if lenght of array is longer than zero
        return False  # If it is true return False
    else: return True # If array is empty return True

array1 = []
array2 = [1, 5, 2, 3]

print(isEmpty(array1))
print(isEmpty(array2))